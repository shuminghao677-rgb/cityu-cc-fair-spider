"""
生成可离线打开的 BI 仪表盘（增强交互版）
将 dashboard_data.json 内嵌到 HTML，生成单个文件，可直接用浏览器打开
"""
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE, "output", "dashboard", "dashboard_data.json")
OUT_PATH = os.path.join(BASE, "output", "dashboard", "dashboard_standalone.html")

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>STEM Fair 2026 招聘 BI 仪表盘</title>
  <script src="https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/echarts.min.js"></script>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #0f1419;
      --card: #1a2332;
      --border: #2d3a4d;
      --text: #e6edf3;
      --muted: #8b949e;
      --accent: #58a6ff;
      --chart-1: #58a6ff;
      --chart-2: #3fb950;
      --chart-3: #d29922;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: 'DM Sans', -apple-system, sans-serif; background: var(--bg); color: var(--text); min-height: 100vh; line-height: 1.5; }
    .header { background: var(--card); border-bottom: 1px solid var(--border); padding: 1rem 2rem; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem; }
    .header h1 { font-size: 1.25rem; font-weight: 600; }
    .header span { color: var(--muted); font-size: 0.9rem; }
    .header-actions { display: flex; gap: 0.5rem; align-items: center; }
    .tabs { display: flex; gap: 0.25rem; padding: 1rem 2rem; border-bottom: 1px solid var(--border); }
    .tab { padding: 0.5rem 1.25rem; background: transparent; border: none; color: var(--muted); cursor: pointer; border-radius: 6px; font-family: inherit; font-size: 0.95rem; transition: all 0.2s; }
    .tab:hover { color: var(--text); background: rgba(88,166,255,0.1); }
    .tab.active { background: var(--border); color: var(--accent); font-weight: 500; }
    .panel { display: none; padding: 1.5rem 2rem 2rem; animation: fadeIn 0.3s ease; }
    .panel.active { display: block; }
    @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
    .grid { display: grid; gap: 1.5rem; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); }
    .card { background: var(--card); border: 1px solid var(--border); border-radius: 10px; padding: 1.25rem; overflow: hidden; transition: transform 0.2s, box-shadow 0.2s; }
    .card:hover { transform: translateY(-2px); box-shadow: 0 8px 24px rgba(0,0,0,0.3); }
    .card h3 { font-size: 0.95rem; font-weight: 600; margin-bottom: 1rem; color: var(--text); display: flex; align-items: center; gap: 0.5rem; }
    .card .filter-row { display: flex; gap: 0.75rem; margin-bottom: 1rem; flex-wrap: wrap; align-items: center; }
    .chart { width: 100%; height: 320px; }
    .chart-lg { height: 420px; }
    select, input[type="search"], input[type="number"] {
      padding: 0.6rem 1rem; background: var(--bg); border: 1px solid var(--border); color: var(--text);
      border-radius: 6px; font-family: inherit; font-size: 0.9rem; min-width: 0;
    }
    select:focus, input:focus { outline: none; border-color: var(--accent); }
    .btn { padding: 0.5rem 1rem; background: var(--border); border: none; color: var(--text); border-radius: 6px; cursor: pointer; font-family: inherit; font-size: 0.85rem; transition: background 0.2s; }
    .btn:hover { background: var(--accent); color: var(--bg); }
    .btn-sm { padding: 0.35rem 0.75rem; font-size: 0.8rem; }
    .badge { display: inline-block; padding: 0.2rem 0.5rem; background: rgba(88,166,255,0.2); color: var(--accent); border-radius: 4px; font-size: 0.75rem; margin-left: 0.5rem; }
    .heat-table { width: 100%; border-collapse: collapse; font-size: 0.8rem; }
    .heat-table th, .heat-table td { padding: 0.4rem 0.6rem; text-align: center; border: 1px solid var(--border); cursor: default; transition: background 0.15s; }
    .heat-table th { background: var(--bg); font-weight: 500; white-space: nowrap; }
    .heat-table tr:hover td { background: rgba(88, 166, 255, 0.1); }
    .heat-table tr.filtered-out { display: none; }
    .heat-table tr.highlight td { background: rgba(88, 166, 255, 0.25) !important; }
    .heat-table .dept { text-align: left; font-size: 0.75rem; max-width: 180px; overflow: hidden; text-overflow: ellipsis; cursor: pointer; }
    .heat-table .dept:hover { color: var(--accent); }
    .heat-table .col-filtered { opacity: 0.4; }
    .heat-table .col-highlight { background: rgba(63, 185, 80, 0.2) !important; font-weight: 600; }
    .search-wrap { flex: 1; min-width: 160px; }
    .search-wrap input { width: 100%; }
    .filter-hint { font-size: 0.8rem; color: var(--muted); }
  </style>
</head>
<body>
  <header class="header">
    <div>
      <h1>STEM Career Fair 2026 招聘分析</h1>
      <span>CityU CCFair 数据仪表盘</span>
    </div>
    <div class="header-actions">
      <span id="filterHint" class="filter-hint" style="display:none"></span>
      <button id="btnReset" class="btn btn-sm" style="display:none">重置筛选</button>
    </div>
  </header>
  <nav class="tabs">
    <button class="tab active" data-panel="edu">学历分析</button>
    <button class="tab" data-panel="tech">技术栈分析</button>
  </nav>
  <main>
    <div id="eduPanel" class="panel active">
      <div class="grid">
        <div class="card">
          <h3>学历要求分布 <span class="badge">点击筛选热力表</span></h3>
          <div id="chartEduDist" class="chart"></div>
        </div>
        <div class="card">
          <h3>专业招聘数量 <span id="topNLabelEdu">TOP 15</span></h3>
          <div class="filter-row">
            <label>显示:</label>
            <select id="topNEdu"><option value="5">TOP 5</option><option value="10">TOP 10</option><option value="15" selected>TOP 15</option><option value="20">TOP 20</option></select>
          </div>
          <div id="chartDeptDist" class="chart"></div>
        </div>
        <div class="card" style="grid-column: 1 / -1;">
          <h3>专业 × 学历 热力表</h3>
          <div class="filter-row">
            <div class="search-wrap"><input type="search" id="searchDept" placeholder="搜索专业名称..."></div>
            <span class="filter-hint">点击上方图表中的专业/学历可筛选</span>
          </div>
          <div style="max-height:420px;overflow:auto">
            <table id="heatEdu" class="heat-table"></table>
          </div>
        </div>
      </div>
    </div>
    <div id="techPanel" class="panel">
      <div class="grid">
        <div class="card">
          <h3>全行业技能需求 <span id="topNLabelTech">TOP 15</span> <span class="badge" id="industryFilterBadge" style="display:none">已按行业筛选</span></h3>
          <div class="filter-row">
            <label>显示:</label>
            <select id="topNTech"><option value="5">TOP 5</option><option value="10">TOP 10</option><option value="15" selected>TOP 15</option><option value="20">TOP 20</option></select>
          </div>
          <div id="chartSkillRank" class="chart"></div>
        </div>
        <div class="card">
          <h3>行业技术栈分布 <span class="badge">点击筛选技能图</span></h3>
          <div id="chartIndustry" class="chart"></div>
        </div>
        <div class="card" style="grid-column: 1 / -1;">
          <h3>按专业查看 TOP 技能</h3>
          <div class="filter-row">
            <div class="search-wrap"><input type="search" id="searchMajor" placeholder="搜索专业..."></div>
            <select id="selectMajor" style="flex:1;min-width:200px"></select>
          </div>
          <div id="chartMajorSkill" class="chart chart-lg"></div>
        </div>
      </div>
    </div>
  </main>
  <script>
    const DATA = __DATA__;
    let state = { filterDept: null, filterEdu: null, filterIndustry: null };

    document.querySelectorAll('.tab').forEach(t => {
      t.onclick = () => {
        document.querySelectorAll('.tab').forEach(x => x.classList.remove('active'));
        document.querySelectorAll('.panel').forEach(x => x.classList.remove('active'));
        t.classList.add('active');
        document.getElementById(t.dataset.panel + 'Panel').classList.add('active');
        if (t.dataset.panel === 'tech') { renderMajorSkill(); renderSkillRank(); }
      };
    });

    function showFilterHint() {
      const parts = [];
      if (state.filterDept) parts.push('专业: ' + state.filterDept);
      if (state.filterEdu) parts.push('学历: ' + state.filterEdu);
      if (state.filterIndustry) parts.push('行业: ' + state.filterIndustry);
      const h = document.getElementById('filterHint');
      const b = document.getElementById('btnReset');
      if (parts.length) { h.textContent = '当前筛选: ' + parts.join(' | '); h.style.display = 'inline'; b.style.display = 'inline'; }
      else { h.style.display = 'none'; b.style.display = 'none'; }
    }
    document.getElementById('btnReset').onclick = () => {
      state = { filterDept: null, filterEdu: null, filterIndustry: null };
      showFilterHint();
      renderHeatEdu();
      renderSkillRank();
      document.getElementById('industryFilterBadge').style.display = 'none';
      if (chartIndustry) chartIndustry.dispatchAction({ type: 'downplay' });
    };

    function barOpt(data, fieldLabel, fieldVal, color) {
      return {
        tooltip: { trigger: 'axis', formatter: p => p.map(d => d.name + ': ' + d.value + ' 个岗位').join('<br/>') },
        grid: { left: '12%', right: '8%', top: '8%', bottom: '15%' },
        xAxis: { type: 'category', data: data.map(d => d[fieldLabel]), axisLabel: { rotate: 35, fontSize: 11 } },
        yAxis: { type: 'value' },
        series: [{ type: 'bar', data: data.map(d => d[fieldVal]), itemStyle: { color }, emphasis: { itemStyle: { borderColor: '#fff', borderWidth: 1 } } }]
      };
    }
    function pieOpt(data, fieldLabel, fieldVal, onClick) {
      const total = data.reduce((s,d) => s + d[fieldVal], 0);
      return {
        tooltip: { trigger: 'item', formatter: p => p.name + ': ' + p.value + ' (' + (total ? (p.value/total*100).toFixed(1) : 0) + '%)' },
        legend: { bottom: 0, type: 'scroll' },
        series: [{
          type: 'pie', radius: ['40%', '70%'],
          data: data.map(d => ({ name: d[fieldLabel], value: d[fieldVal] })),
          label: { fontSize: 11 }, emphasis: { itemStyle: { shadowBlur: 10, shadowOffsetX: 0 } }
        }]
      };
    }

    let chartEduDist, chartDeptDist, chartSkillRank, chartIndustry, chartMajorSkill;

    function renderEduDist() {
      chartEduDist = echarts.init(document.getElementById('chartEduDist'));
      const d = DATA.education.edu_level_distribution;
      const opt = pieOpt(d, 'education_level', 'count');
      chartEduDist.setOption(opt);
      chartEduDist.off('click');
      chartEduDist.on('click', p => {
        if (p.name) { state.filterEdu = state.filterEdu === p.name ? null : p.name; showFilterHint(); renderHeatEdu(); }
      });
    }

    function renderDeptDist() {
      const n = parseInt(document.getElementById('topNEdu').value) || 15;
      document.getElementById('topNLabelEdu').textContent = 'TOP ' + n;
      if (!chartDeptDist) chartDeptDist = echarts.init(document.getElementById('chartDeptDist'));
      const d = DATA.education.department_distribution.slice(0, n);
      chartDeptDist.setOption(barOpt(d, 'department', 'count', '#58a6ff'));
      chartDeptDist.off('click');
      chartDeptDist.on('click', p => {
        if (p.componentType === 'series' && p.name) {
          state.filterDept = state.filterDept === p.name ? null : p.name;
          showFilterHint();
          renderHeatEdu();
        }
      });
    }
    document.getElementById('topNEdu').onchange = renderDeptDist;

    function renderHeatEdu() {
      const p = DATA.education.pivot;
      const maxVal = Math.max(...p.matrix.flat());
      const rows = p.departments;
      const cols = p.edu_levels;
      const search = (document.getElementById('searchDept') || {}).value || '';
      const searchLower = search.toLowerCase();
      let html = '<tr><th>专业</th>' + cols.map(c => {
        const isHighlight = state.filterEdu && c === state.filterEdu;
        return '<th class="' + (isHighlight ? 'col-highlight' : '') + '">' + c + '</th>';
      }).join('') + '</tr>';
      rows.forEach(dept => {
        const matchSearch = !searchLower || dept.toLowerCase().includes(searchLower);
        const matchDept = !state.filterDept || dept === state.filterDept;
        const show = matchSearch && matchDept;
        const isHighlight = state.filterDept && dept === state.filterDept;
        html += '<tr class="' + (show ? '' : 'filtered-out') + (isHighlight ? ' highlight' : '') + '" data-dept="' + dept.replace(/"/g,'&quot;') + '">';
        html += '<td class="dept" title="' + dept + '">' + dept + '</td>';
        cols.forEach((col, j) => {
          const v = p.matrix[p.departments.indexOf(dept)][j];
          const intensity = maxVal ? (v / maxVal) : 0;
          const bg = 'rgba(88,166,255,' + (0.2 + intensity * 0.6) + ')';
          const cellClass = state.filterEdu && col === state.filterEdu ? ' col-highlight' : '';
          html += '<td class="' + cellClass + '" style="background:' + bg + '" data-edu="' + col.replace(/"/g,'&quot;') + '">' + v + '</td>';
        });
        html += '</tr>';
      });
      const el = document.getElementById('heatEdu');
      if (el) el.innerHTML = html;
      el.querySelectorAll('.dept').forEach(td => {
        td.onclick = () => { state.filterDept = state.filterDept === td.closest('tr').dataset.dept ? null : td.closest('tr').dataset.dept; showFilterHint(); renderHeatEdu(); };
      });
    }
    (document.getElementById('searchDept') || {}).oninput = renderHeatEdu;

    function renderSkillRank() {
      const n = parseInt(document.getElementById('topNTech').value) || 15;
      document.getElementById('topNLabelTech').textContent = 'TOP ' + n;
      let d;
      if (state.filterIndustry) {
        const bySkill = {};
        DATA.technical.industry_skill.filter(x => x.industry === state.filterIndustry).forEach(x => {
          bySkill[x.skill] = (bySkill[x.skill] || 0) + x.frequency;
        });
        d = Object.entries(bySkill).map(([skill, frequency]) => ({ skill, frequency })).sort((a,b) => b.frequency - a.frequency).slice(0, n);
        document.getElementById('industryFilterBadge').style.display = 'inline';
      } else {
        d = DATA.technical.skill_ranking.slice(0, n);
        document.getElementById('industryFilterBadge').style.display = 'none';
      }
      if (!chartSkillRank) chartSkillRank = echarts.init(document.getElementById('chartSkillRank'));
      chartSkillRank.setOption(barOpt(d, 'skill', 'frequency', '#3fb950'));
    }
    document.getElementById('topNTech').onchange = renderSkillRank;

    function renderIndustry() {
      chartIndustry = echarts.init(document.getElementById('chartIndustry'));
      const d = DATA.technical.industry_distribution;
      const opt = pieOpt(d, 'industry', 'count');
      chartIndustry.setOption(opt);
      chartIndustry.off('click');
      chartIndustry.on('click', p => {
        if (p.name) { state.filterIndustry = state.filterIndustry === p.name ? null : p.name; showFilterHint(); renderSkillRank(); }
      });
    }

    function renderMajorSelect() {
      const majors = Object.keys(DATA.technical.top_skills_by_major).sort();
      const sel = document.getElementById('selectMajor');
      const search = (document.getElementById('searchMajor') || {}).value || '';
      const searchLower = search.toLowerCase();
      const filtered = searchLower ? majors.filter(m => m.toLowerCase().includes(searchLower)) : majors;
      sel.innerHTML = filtered.map(m => '<option value="' + m + '">' + m + '</option>').join('');
      if (filtered.length && !filtered.includes(sel.value)) sel.value = filtered[0];
      sel.onchange = renderMajorSkill;
    }
    (document.getElementById('searchMajor') || {}).oninput = renderMajorSelect;

    function renderMajorSkill() {
      const major = document.getElementById('selectMajor').value;
      const skills = DATA.technical.top_skills_by_major[major] || [];
      if (!chartMajorSkill) chartMajorSkill = echarts.init(document.getElementById('chartMajorSkill'));
      chartMajorSkill.setOption(barOpt(skills, 'skill', 'frequency', '#d29922'));
    }

    window.addEventListener('resize', () => {
      [chartEduDist, chartDeptDist, chartSkillRank, chartIndustry, chartMajorSkill].forEach(c => c && c.resize());
    });

    renderEduDist();
    renderDeptDist();
    renderHeatEdu();
    renderSkillRank();
    renderIndustry();
    renderMajorSelect();
    renderMajorSkill();
  </script>
</body>
</html>
'''

def main():
    if not os.path.exists(JSON_PATH):
        print(f"错误: 请先运行 python run_analysis.py 生成 {JSON_PATH}")
        return
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    html = HTML_TEMPLATE.replace("__DATA__", json.dumps(data, ensure_ascii=False))
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✓ 已生成可离线仪表盘（增强交互版）: {OUT_PATH}")
    print("  可直接用浏览器打开，无需启动服务器")

if __name__ == "__main__":
    main()
