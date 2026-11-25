<!DOCTYPE html>
<html lang="mn">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>10-р анги | 1.1 Хөрөг найрууллын тухай юу мэдэх вэ?</title>
  <style>
    * {
      box-sizing: border-box;
    }
    body {
      margin: 0;
      font-family: "Segoe UI", Arial, sans-serif;
      background: #f3f6fa;
      color: #1e293b;
      line-height: 1.7;
    }
    header {
      background: linear-gradient(135deg, #0f172a, #1d4ed8);
      color: #ffffff;
      padding: 32px 20px;
      text-align: center;
    }
    .badge {
      display: inline-block;
      background: rgba(255, 255, 255, 0.18);
      padding: 4px 12px;
      border-radius: 20px;
      font-size: 13px;
      margin-bottom: 8px;
    }
    header h1 {
      margin: 4px 0 8px;
      font-size: 25px;
    }
    header p {
      margin: 0;
      font-size: 15px;
      opacity: 0.9;
    }
    nav {
      display: flex;
      justify-content: center;
      gap: 10px;
      background: #ffffff;
      padding: 12px 16px;
      border-bottom: 1px solid #e2e8f0;
      flex-wrap: wrap;
      position: sticky;
      top: 0;
      z-index: 10;
    }
    nav button {
      background: #f1f5f9;
      color: #334155;
      border: 1px solid #cbd5e1;
      padding: 9px 15px;
      border-radius: 8px;
      cursor: pointer;
      font-weight: 600;
      font-size: 14px;
      transition: 0.2s;
    }
    nav button.active,
    nav button:hover {
      background: #1d4ed8;
      color: #ffffff;
      border-color: #1d4ed8;
    }
    main {
      max-width: 880px;
      margin: 28px auto;
      padding: 0 18px 40px;
    }
    .section {
      display: none;
      background: #ffffff;
      padding: 28px;
      border-radius: 14px;
      box-shadow: 0 4px 18px rgba(15, 23, 42, 0.06);
    }
    .section.active {
      display: block;
    }
    h2 {
      margin-top: 0;
      color: #1e3a8a;
      font-size: 21px;
      border-bottom: 2px solid #eff6ff;
      padding-bottom: 8px;
    }
    h3 {
      color: #0f172a;
      font-size: 17px;
      margin-top: 20px;
    }
    .goal-box {
      background: #eff6ff;
      border-left: 4px solid #2563eb;
      padding: 14px 18px;
      border-radius: 8px;
      margin-bottom: 20px;
    }
    .grid-2 {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 16px;
      margin: 16px 0;
    }
    .info-card {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 10px;
      padding: 16px;
    }
    .info-card h4 {
      margin: 0 0 8px;
      color: #1d4ed8;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 12px;
      font-size: 15px;
    }
    th, td {
      border: 1px solid #cbd5e1;
      padding: 10px 12px;
      text-align: left;
    }
    th {
      background: #f1f5f9;
      color: #1e3a8a;
    }
    .reading-box {
      background: #fffbeb;
      border: 1px solid #fde68a;
      padding: 18px;
      border-radius: 10px;
      margin: 14px 0;
    }
    .highlight-fact {
      background: #dbeafe;
      padding: 2px 5px;
      border-radius: 4px;
    }
    .highlight-art {
      background: #dcfce7;
      padding: 2px 5px;
      border-radius: 4px;
    }
    .action-btn {
      background: #1d4ed8;
      color: #ffffff;
      border: none;
      padding: 10px 18px;
      border-radius: 8px;
      cursor: pointer;
      font-size: 14px;
      font-weight: 600;
      margin-top: 10px;
      margin-right: 8px;
    }
    .action-btn:hover {
      background: #1e40af;
    }
    .secondary-btn {
      background: #e2e8f0;
      color: #1e293b;
    }
    .secondary-btn:hover {
      background: #cbd5e1;
    }
    .analysis-result {
      display: none;
      background: #f8fafc;
      border: 1px solid #cbd5e1;
      padding: 16px;
      border-radius: 10px;
      margin-top: 14px;
    }
    .form-group {
      margin-bottom: 14px;
    }
    .form-group label {
      display: block;
      font-weight: 600;
      margin-bottom: 6px;
    }
    .form-group input,
    .form-group textarea {
      width: 100%;
      padding: 10px;
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      font-family: inherit;
      font-size: 14px;
    }
    .question {
      margin-bottom: 18px;
      padding-bottom: 14px;
      border-bottom: 1px solid #f1f5f9;
    }
    .question p {
      font-weight: 600;
      margin-bottom: 8px;
    }
    .question label {
      display: block;
      margin: 5px 0;
      cursor: pointer;
    }
    #quizResult {
      margin-top: 16px;
      padding: 14px;
      border-radius: 8px;
      font-weight: 600;
      display: none;
    }
  </style>
</head>
<body>

  <header>
    <div class="badge">Монгол хэл • 10-р анги • I бүлэг</div>
    <h1>1.1 Хөрөг найрууллын тухай юу мэдэх вэ?</h1>
    <p>1. Уран зохиолын бус эхийг задлан шинжилж, бичиж суръя</p>
  </header>

  <nav>
    <button class="tab-btn active" onclick="openTab('theory', this)">1. Онол ба онцлог</button>
    <button class="tab-btn" onclick="openTab('analysis', this)">2. Эх задлан шинжлэх</button>
    <button class="tab-btn" onclick="openTab('plan', this)">3. Бичих төлөвлөлт</button>
    <button class="tab-btn" onclick="openTab('quiz', this)">4. Мэдлэг шалгах сорил</button>
  </nav>

  <main>
    <!-- 1-р хэсэг: Онолын мэдлэг -->
    <section id="theory" class="section active">
      <h2>Хөрөг найруулал гэж юу вэ?</h2>
      <div class="goal-box">
        <strong>Хичээлийн зорилго:</strong> Уран зохиолын бус эхийн нэг төрөл болох хөрөг найрууллын онцлог, бүтэц, хэл найруулгын шинжийг таньж, жишээ эхэд задлал хийж сурна.
      </div>

      <p><strong>Хөрөг найруулал</strong> нь сонин нийтлэлийн найруулгын уран сайхны нийтлэлийн төрөлд хамаарах бөгөөд <strong>бодит хүний</strong> ажил үйлс, зан чанар, үзэл бодол, дотоод ертөнцийг баримтад тулгуурлан уран сайхны аргаар дүрслэн харуулсан эх юм.</p>

      <div class="grid-2">
        <div class="info-card">
          <h4>1. Бодит баримтад тулгуурлана</h4>
          <p>Зохиомол дүр биш; тухайн хүний нэр, ажил мэргэжил, амьдралын бодит үйл явдал, хэлсэн үг, баримт сэлтийг үнэн зөв тусгана.</p>
        </div>
        <div class="info-card">
          <h4>2. Уран сайхны дүрслэл ашиглана</h4>
          <p>Зөвхөн намтар тоочих бус, дүрслэх ур маяг (зүйрлэл, эпитет, хэлц үг), орчны зураглал, сэтгэл хөдлөлөөр баатрыг амьд мэт харуулна.</p>
        </div>
      </div>

      <h3>Хөрөг найрууллын бүтэц</h3>
      <table>
        <thead>
          <tr>
            <th>Бүтцийн хэсэг</th>
            <th>Агуулгын үүрэг</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Эхлэл хэсэг</strong></td>
            <td>Баатрыг уншигчид танилцуулах, анхаарал татах онцлог дүр зураг эсвэл сонирхолтой баримтаар эхэлнэ.</td>
          </tr>
          <tr>
            <td><strong>Гол хэсэг</strong></td>
            <td>Баатрын зан чанар, ажил хөдөлмөрийн амжилт, бэрхшээлийг даван туулсан түүх, яриа, үйлдлийг баримт ба дүрслэлээр нээнэ.</td>
          </tr>
          <tr>
            <td><strong>Төгсгөл хэсэг</strong></td>
            <td>Баатрын нийгэмд оруулж буй үнэ цэнэ, зохиогчийн дүгнэлт, уншигчид төрүүлэх бахархал, ухаарлаар өндөрлөнө.</td>
          </tr>
        </tbody>
      </table>
    </section>

    <!-- 2-р хэсэг: Эх задлан шинжлэх -->
    <section id="analysis" class="section">
      <h2>Дасгал: Хөрөг найрууллын хэсгийг задлан шинжилье</h2>
      <p>Дараах жишээ хэсгийг анхааралтай уншаад, <strong>бодит баримт</strong> болон <strong>уран дүрслэл</strong> хэрхэн хосолсныг ажиглаарай.</p>

      <div class="reading-box" id="sampleText">
        <p>«Үүр цүүрээр хөдөөгийн талд мөнгөн шүүдэр гялтганаж байхад тэр хэдийнээ хониныхоо бэлчээрт гарчихсан явна. Гучин таван жил тасралтгүй мал малласан түүний гарын алга ширүүн ч гэлээ төл мал бүрээ нэрээр нь дуудах мэт энхрий зөөлөн ааштай. "Мал дагавал ам тосдоно гэдэг чинь зүгээр нэг үг биш, хөдөлмөрийн үр шим юм шүү" хэмээн тэр инээмсэглэн өгүүлэв. Сүүлийн таван жилд тэрээр сумынхаа залуу малчдад мал маллагааны арга ухаанаас зааж, хорин гаруй шавь бэлтгэжээ.»</p>
      </div>

      <button class="action-btn" onclick="highlightElements()">Баримт ба дүрслэлийг ялгаж харах</button>
      <button class="action-btn secondary-btn" onclick="toggleAnalysis()">Задлалын тайлбар харах</button>

      <div id="legend" style="display:none; margin-top:12px; font-size:14px;">
        <span class="highlight-fact">Цэнхэр дэвсгэр</span> — Бодит баримт, тоо, эшлэл &nbsp;|&nbsp;
        <span class="highlight-art">Ногоон дэвсгэр</span> — Уран сайхны дүрслэл, орчны зураглал
      </div>

      <div id="analysisBox" class="analysis-result">
        <h4>Эхийн задлал:</h4>
        <ul>
          <li><strong>Сэдэв, гол санаа:</strong> Хөдөлмөрч малчны ажилч хичээнгүй чанар, залуу хойч үедээ өвлүүлж буй туршлагыг бахархан харуулсан.</li>
          <li><strong>Баримтын хэрэглээ:</strong> «Гучин таван жил», «таван жилд», «хорин гаруй шавь» зэрэг бодит тоо баримт болон баатрын шууд яриаг оруулсан нь эхийг үнэмшилтэй болгожээ.</li>
          <li><strong>Дүрслэх ур маяг:</strong> «Мөнгөн шүүдэр гялтганаж», «гарын алга ширүүн ч гэлээ... энхрий зөөлөн ааштай» гэх зэргээр гадаад байдал, дотоод сэтгэлийг уран сайхнаар тодотгосон байна.</li>
        </ul>
      </div>
    </section>

    <!-- 3-р хэсэг: Бичих төлөвлөлт -->
    <section id="plan" class="section">
      <h2>Бүтээлч даалгавар: Хөрөг найрууллын төлөвлөгөө гаргах</h2>
      <p>Чи хөрөг найруулал бичихээр сонгосон бодит хүнийхээ талаар доорх асуултын дагуу тэмдэглэл хөтөлж, төлөвлөгөөгөө бэлтгээрэй.</p>

      <div class="form-group">
        <label>1. Хөрөглөн бичих баатар хэн бэ? (Нэр, нас, ажил мэргэжил)</label>
        <input type="text" id="heroName" placeholder="Жишээ нь: Манай сургуулийн ахмад багш Д.Болд..." />
      </div>

      <div class="form-group">
        <label>2. Түүнийг бусдаас ялгаруулах гол зан чанар, онцлог юу вэ?</label>
        <input type="text" id="heroTrait" placeholder="Жишээ нь: Тууштай, хүн бүрт чин сэтгэлээсээ тусалдаг..." />
      </div>

      <div class="form-group">
        <label>3. Оруулах бодит баримт, үйл явдал, хэлсэн онцлох үг:</label>
        <textarea id="heroFact" rows="3" placeholder="Жишээ нь: 25 жил багшилсан, шавь нар нь улсын олимпиадад түрүүлсэн..."></textarea>
      </div>

      <button class="action-btn" onclick="generateOutline()">Төлөвлөгөө үүсгэх</button>
      <div id="outlineOutput" class="analysis-result"></div>
    </section>

    <!-- 4-р хэсэг: Сорил -->
    <section id="quiz" class="section">
      <h2>Мэдлэг шалгах сорил</h2>

      <div class="question">
        <p>1. Хөрөг найруулал нь ямар төрлийн эхэд хамаарах вэ?</p>
        <label><input type="radio" name="q1" value="a"> А. Зөвхөн уран зохиолын зохиомол эх</label>
        <label><input type="radio" name="q1" value="b"> Б. Уран зохиолын бус эх (сонин нийтлэлийн уран сайхны төрөл)</label>
        <label><input type="radio" name="q1" value="c"> В. Албан бичгийн эх</label>
      </div>

      <div class="question">
        <p>2. Хөрөг найрууллын гол судлагдахуун буюу дүр нь хэн байдаг вэ?</p>
        <label><input type="radio" name="q2" value="a"> А. Зохиолчийн төсөөлөн бодсон баатар</label>
        <label><input type="radio" name="q2" value="b"> Б. Түүхэн домог, үлгэрийн баатар</label>
        <label><input type="radio" name="q2" value="c"> В. Бодит амьдрал дээрх хувь хүн, түүний ажил үйлс, дотоод ертөнц</label>
      </div>

      <div class="question">
        <p>3. Хөрөг найруулал нь энгийн намтар, товч танилцуулгаас юугаараа ялгаатай вэ?</p>
        <label><input type="radio" name="q3" value="a"> А. Баримтыг уран сайхны дүрслэл, сэтгэл хөдлөлтэй хослуулан бичдэгээрээ</label>
        <label><input type="radio" name="q3" value="b"> Б. Он сар өдөр огт дурддаггүйгээрээ</label>
        <label><input type="radio" name="q3" value="c"> В. Зөвхөн хүснэгт хэлбэрээр бичдэгээрээ</label>
      </div>

      <div class="question">
        <p>4. Баатрын хэлсэн үгийг (эшлэлийг) хөрөг найруулалд оруулахын гол ач холбогдол юу вэ?</p>
        <label><input type="radio" name="q4" value="a"> А. Эхийн үгийн тоог нэмэх</label>
        <label><input type="radio" name="q4" value="b"> Б. Баатрын үзэл бодол, зан төрхийг бодитой, амьд болгож харуулах</label>
        <label><input type="radio" name="q4" value="c"> В. Албан бичгийн шинжтэй болгох</label>
      </div>

      <button class="action-btn" onclick="gradeQuiz()">Дүнгээ шалгах</button>
      <div id="quizResult"></div>
    </section>
  </main>

  <script>
    function openTab(sectionId, btn) {
      document.querySelectorAll('.section').forEach(sec => sec.classList.remove('active'));
      document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
      document.getElementById(sectionId).classList.add('active');
      btn.classList.add('active');
    }

    let isHighlighted = false;
    function highlightElements() {
      const box = document.getElementById('sampleText');
      const legend = document.getElementById('legend');
      if (!isHighlighted) {
        box.innerHTML = `<p>«<span class="highlight-art">Үүр цүүрээр хөдөөгийн талд мөнгөн шүүдэр гялтганаж байхад</span> тэр хэдийнээ хониныхоо бэлчээрт гарчихсан явна. <span class="highlight-fact">Гучин таван жил тасралтгүй мал малласан</span> түүний <span class="highlight-art">гарын алга ширүүн ч гэлээ төл мал бүрээ нэрээр нь дуудах мэт энхрий зөөлөн ааштай.</span> <span class="highlight-fact">"Мал дагавал ам тосдоно гэдэг чинь зүгээр нэг үг биш, хөдөлмөрийн үр шим юм шүү"</span> хэмээн тэр инээмсэглэн өгүүлэв. <span class="highlight-fact">Сүүлийн таван жилд тэрээр сумынхаа залуу малчдад мал маллагааны арга ухаанаас зааж, хорин гаруй шавь бэлтгэжээ.</span>»</p>`;
        legend.style.display = 'block';
        isHighlighted = true;
      } else {
        box.innerHTML = `<p>«Үүр цүүрээр хөдөөгийн талд мөнгөн шүүдэр гялтганаж байхад тэр хэдийнээ хониныхоо бэлчээрт гарчихсан явна. Гучин таван жил тасралтгүй мал малласан түүний гарын алга ширүүн ч гэлээ төл мал бүрээ нэрээр нь дуудах мэт энхрий зөөлөн ааштай. "Мал дагавал ам тосдоно гэдэг чинь зүгээр нэг үг биш, хөдөлмөрийн үр шим юм шүү" хэмээн тэр инээмсэглэн өгүүлэв. Сүүлийн таван жилд тэрээр сумынхаа залуу малчдад мал маллагааны арга ухаанаас зааж, хорин гаруй шавь бэлтгэжээ.»</p>`;
        legend.style.display = 'none';
        isHighlighted = false;
      }
    }

    function toggleAnalysis() {
      const box = document.getElementById('analysisBox');
      box.style.display = box.style.display === 'none' || box.style.display === '' ? 'block' : 'none';
    }

    function generateOutline() {
      const name = document.getElementById('heroName').value.trim();
      const trait = document.getElementById('heroTrait').value.trim();
      const fact = document.getElementById('heroFact').value.trim();
      const out = document.getElementById('outlineOutput');

      if (!name || !trait || !fact) {
        out.style.display = 'block';
        out.innerHTML = `<p style="color:#b91c1c;">Бүх гурван талбарыг бөглөөд төлөвлөгөөгөө үүсгэнэ үү.</p>`;
        return;
      }

      out.style.display = 'block';
      out.innerHTML = `
        <h4>Чиний хөрөг найрууллын бүтцийн ноорог:</h4>
        <p><strong>1. Эхлэл:</strong> ${name} хүний онцлог дүр төрх, анхны сэтгэгдэл төрүүлэх орчны зураглалаар эхэлнэ.</p>
        <p><strong>2. Гол хэсэг:</strong> Түүний <em>«${trait}»</em> зан чанарыг харуулахын тулд <em>«${fact}»</em> зэрэг бодит баримт, яриаг дэлгэрүүлэн бичнэ.</p>
        <p><strong>3. Төгсгөл:</strong> Энэ хүнээс суралцах зүйл, бахархах сэтгэгдлээр эхээ дүгнэн төгсгөнө.</p>
      `;
    }

    function gradeQuiz() {
      const answers = { q1: 'b', q2: 'c', q3: 'a', q4: 'b' };
      let score = 0;

      for (let q in answers) {
        const chosen = document.querySelector(`input[name="${q}"]:checked`);
        if (chosen && chosen.value === answers[q]) {
          score++;
        }
      }

      const resultBox = document.getElementById('quizResult');
      resultBox.style.display = 'block';
      resultBox.style.background = score === 4 ? '#dcfce7' : '#fef9c3';
      resultBox.textContent = `Та 4 асуултаас ${score} зөв хариуллаа!`;
    }
  </script>

</body>
</html>