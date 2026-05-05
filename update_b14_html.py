#!/usr/bin/env python3
"""Update B14 review-briefing.html — patch the 20 corrected ads (10 winner vars + 10 native images)."""

import re
from pathlib import Path

HTML_PATH = Path("/tmp/tmc-ads-review/index.html")
html = HTML_PATH.read_text()

# ─────────────────────────────────────────────────
# UPDATED AD DATA  (only fields that changed)
# ─────────────────────────────────────────────────
UPDATES = {
    # ── WINNER VARIATIONS ────────────────────────
    1: dict(
        title_en="Winner Var 1: Reference — Gray T-Shirt (Shirt Pull)",
        title_pt="Winner Var 1: Referência — Camiseta Cinza (Puxando a Camisa)",
        angle_en="Wife Testimonial — 2:15 AM bedroom / post-intimacy sweat (reference photo baseline)",
        angle_pt="Testemunho da Esposa — quarto 2:15 AM / suor pós-intimidade (referência baseline)",
        hookVisual_en="Torso shot, collarbone to upper thigh, no face. Gray heather t-shirt soaked through with large wet patches. Right hand pulling shirt fabric slightly outward, wedding ring clearly visible. Clock 2:15 AM on nightstand. Warm amber lamp. Unmade bed at edge. Raw iPhone aesthetic. 4:5 vertical.",
        hookVisual_pt="Torso, do colarinho à coxa, sem rosto. Camiseta cinza encharcada com grandes manchas. Mão direita puxando o tecido, aliança claramente visível. Relógio 2:15 AM na mesinha. Luz âmbar quente. Cama desfeita na borda. Estética iPhone crua. 4:5 vertical.",
        format_en="Native long-form image (raw phone photo) | Winner Variation",
        format_pt="Imagem native long-form (foto crua de celular) | Winner Variation",
        execution_en="Copy VERBATIM from session. BASELINE — all other variations test against this one.",
        execution_pt="Copy VERBATIM da sessão. BASELINE — todas as outras variações testam contra esta.",
    ),
    2: dict(
        title_en="Winner Var 2: White Ribbed Tank Top",
        title_pt="Winner Var 2: Regata Branca Canelada",
        hookVisual_en="Same reference composition — torso shot, no face. White ribbed cotton tank top (form-fitting) soaked through. Sweat shows dramatically on white — high-contrast wet patches. One hand pulling fabric, wedding ring visible. Clock 2:15 AM. Warm lamp. Messy bed. Same brunette hair. 4:5 vertical.",
        hookVisual_pt="Mesma composição — torso sem rosto. Regata branca canelada encharcada. Manchas de suor de alto contraste no branco. Mão puxando o tecido, aliança visível. Relógio 2:15 AM. Luz quente. Cama desfeita. 4:5 vertical.",
        format_en="Native long-form image (raw phone photo) | Winner Variation",
        format_pt="Imagem native long-form (foto crua de celular) | Winner Variation",
        execution_en="Copy VERBATIM. Test: Does high-contrast white-on-wet sweat visibility outperform gray? White = more shocking, less ambiguous.",
        execution_pt="Copy VERBATIM. Teste: Alta visibilidade do suor no branco supera o cinza? Branco = mais chocante, menos ambíguo.",
    ),
    13: dict(
        title_en="Winner Var 3: Soaked Hair Close-Up",
        title_pt="Winner Var 3: Close-Up do Cabelo Encharcado",
        hookVisual_en="Camera angle raised — frame from shoulders to just below jaw, no full face. Dark brunette hair soaked and matted, strands clinging to neck and collarbone. Hair is primary sweat evidence. Same gray t-shirt at bottom. One hand near neck, wedding ring visible. Clock 2:15 AM. Warm lamp. Raw iPhone aesthetic.",
        hookVisual_pt="Ângulo levantado — enquadramento dos ombros até abaixo do queixo, sem rosto completo. Cabelo castanho encharcado e grudado no pescoço e clavícula. Cabelo é a evidência principal de suor. Camiseta cinza visível na parte inferior. Aliança visível. Relógio 2:15 AM.",
        format_en="Native long-form image (raw phone photo) | Winner Variation",
        format_pt="Imagem native long-form (foto crua de celular) | Winner Variation",
        execution_en="Copy VERBATIM. Test: Does hair-as-sweat-evidence (implies total-body exertion) feel more intense than shirt-as-sweat-evidence?",
        execution_pt="Copy VERBATIM. Teste: Cabelo como evidência de suor (implica esforço corporal total) parece mais intenso que a camisa?",
    ),
    14: dict(
        title_en="Winner Var 4: Blonde Hair",
        title_pt="Winner Var 4: Cabelo Loiro",
        hookVisual_en="Same reference composition exactly — torso shot, no face. Gray heather t-shirt soaked through, hand pulling shirt outward, wedding ring visible. Same bedroom, clock 2:15 AM, messy bed. Only change: blonde hair — disheveled, slightly damp at roots and ends, falling past shoulder. 4:5 vertical.",
        hookVisual_pt="Mesma composição exata — torso sem rosto. Camiseta cinza encharcada, mão puxando, aliança visível. Mesmo quarto, relógio 2:15 AM, cama desfeita. Única mudança: cabelo loiro — despenteado, levemente úmido. 4:5 vertical.",
        format_en="Native long-form image (raw phone photo) | Winner Variation",
        format_pt="Imagem native long-form (foto crua de celular) | Winner Variation",
        execution_en="Copy VERBATIM. Test: Does blonde hair expand demographic resonance vs brunette baseline?",
        execution_pt="Copy VERBATIM. Teste: Cabelo loiro expande o alcance demográfico vs castanho?",
    ),
    25: dict(
        title_en="Winner Var 5: Black T-Shirt",
        title_pt="Winner Var 5: Camiseta Preta",
        hookVisual_en="Same reference composition — torso shot, no face. Black cotton t-shirt, soaked. Sweat visible as slightly darker wet patches (subtle on black — less high-contrast). Hand pulling shirt outward, wedding ring visible. Clock 2:15 AM. Warm lamp. Messy bed. Brunette hair. 4:5 vertical.",
        hookVisual_pt="Mesma composição — torso sem rosto. Camiseta preta encharcada. Suor visível como manchas mais escuras (sutil no preto). Mão puxando, aliança visível. Relógio 2:15 AM. 4:5 vertical.",
        format_en="Native long-form image (raw phone photo) | Winner Variation",
        format_pt="Imagem native long-form (foto crua de celular) | Winner Variation",
        execution_en="Copy VERBATIM. Test: Does lower sweat visibility on black create more curiosity vs obvious sweat on gray? Mystery vs. shock.",
        execution_pt="Copy VERBATIM. Teste: Menor visibilidade do suor no preto cria mais curiosidade vs suor óbvio no cinza? Mistério vs choque.",
    ),
    26: dict(
        title_en="Winner Var 6: Oversized Men's T-Shirt",
        title_pt="Winner Var 6: Camiseta Masculina Oversized",
        hookVisual_en="Same reference composition — torso, no face. Woman wearing an oversized men's t-shirt — clearly not hers (neckline droops off one shoulder, sleeves hang past elbow). Soaked through. Hand gathers oversized fabric and pulls outward, wedding ring visible. Clock 2:15 AM. Warm lamp. Messy bed. 4:5 vertical.",
        hookVisual_pt="Mesma composição — torso sem rosto. Mulher com camiseta masculina oversized — claramente não é dela (gola tombando, mangas longas). Encharcada. Mão junta o tecido e puxa, aliança visível. Relógio 2:15 AM. 4:5 vertical.",
        format_en="Native long-form image (raw phone photo) | Winner Variation",
        format_pt="Imagem native long-form (foto crua de celular) | Winner Variation",
        execution_en="Copy VERBATIM. Test: Does 'wearing his shirt' (post-intimacy ownership cue) create stronger emotional signal than wearing her own shirt?",
        execution_pt="Copy VERBATIM. Teste: 'Vestindo a camisa dele' (sinal de posse pós-intimidade) gera sinal emocional mais forte?",
    ),
    37: dict(
        title_en="Winner Var 7: Red/Auburn Hair",
        title_pt="Winner Var 7: Cabelo Ruivo/Acobreado",
        hookVisual_en="Same reference composition exactly — torso shot, no face. Gray heather t-shirt soaked through, hand pulling shirt outward, wedding ring visible. Same bedroom, clock 2:15 AM, messy bed. Only change: red/auburn hair — disheveled, slightly damp, waves or slight curl, falling past shoulder. 4:5 vertical.",
        hookVisual_pt="Mesma composição exata — torso sem rosto. Camiseta cinza encharcada, aliança visível. Única mudança: cabelo ruivo/acobreado — despenteado, levemente úmido, ondulado. 4:5 vertical.",
        format_en="Native long-form image (raw phone photo) | Winner Variation",
        format_pt="Imagem native long-form (foto crua de celular) | Winner Variation",
        execution_en="Copy VERBATIM. Test: Does hair color (red vs brunette vs blonde) affect performance? Three-way color test with V1/V4/V7.",
        execution_pt="Copy VERBATIM. Teste: Cor do cabelo (ruivo vs castanho vs loiro) afeta performance? Teste triplo com V1/V4/V7.",
    ),
    38: dict(
        title_en="Winner Var 8: Messy Bun — Sweaty Flyaways",
        title_pt="Winner Var 8: Coque Bagunçado — Fios Suados",
        hookVisual_en="Camera angle raised — frame from mid-chest to just below chin/jaw. Hair thrown up in hasty messy bun — improvised, asymmetric, loose strands falling. Sweaty flyaways sticking to temples and back of neck. Same gray t-shirt, soaked. Wedding ring visible. Clock 2:15 AM in background. Raw iPhone aesthetic. 4:5 vertical.",
        hookVisual_pt="Ângulo levantado — enquadramento do meio do peito até o queixo. Cabelo jogado em coque bagunçado — improvisado, assimétrico. Fios suados grudados nas têmporas e pescoço. Camiseta cinza encharcada. Aliança visível. Relógio 2:15 AM. 4:5 vertical.",
        format_en="Native long-form image (raw phone photo) | Winner Variation",
        format_pt="Imagem native long-form (foto crua de celular) | Winner Variation",
        execution_en="Copy VERBATIM. Test: Does 'threw hair up to cool down' gesture signal higher intensity of exertion than hair-down?",
        execution_pt="Copy VERBATIM. Teste: 'Prendeu o cabelo pra refrescar' sinaliza maior intensidade do que cabelo solto?",
    ),
    49: dict(
        title_en="Winner Var 9: Navy Athletic Tank",
        title_pt="Winner Var 9: Regata Esportiva Navy",
        hookVisual_en="Same reference composition — torso shot, no face. Navy athletic/sport tank top (form-fitting, soaked through across chest and under arms). Hand pulling or gathering fabric, wedding ring visible. Clock 2:15 AM. Warm lamp. Messy bed. Brunette hair, disheveled. 4:5 vertical.",
        hookVisual_pt="Mesma composição — torso sem rosto. Regata esportiva navy encharcada no peito e axilas. Mão puxando o tecido, aliança visível. Relógio 2:15 AM. Luz quente. Cama desfeita. 4:5 vertical.",
        format_en="Native long-form image (raw phone photo) | Winner Variation",
        format_pt="Imagem native long-form (foto crua de celular) | Winner Variation",
        execution_en="Copy VERBATIM. Test: Does sportswear imply higher intensity of physical exertion vs everyday t-shirt, amplifying the subtext?",
        execution_pt="Copy VERBATIM. Teste: Roupa esportiva implica maior intensidade de esforço vs camiseta comum?",
    ),
    50: dict(
        title_en="Winner Var 10: Drinking Water",
        title_pt="Winner Var 10: Bebendo Água",
        hookVisual_en="Same reference composition — torso shot, no face. Gray heather t-shirt soaked through. Both hands visible: one holds a glass of water at chest height (just finished drinking — slightly tilted, condensated). Wedding ring on one hand. Clock 2:15 AM. Warm lamp. Messy bed. Hair disheveled. 4:5 vertical.",
        hookVisual_pt="Mesma composição — torso sem rosto. Camiseta cinza encharcada. Ambas as mãos visíveis: uma segura copo d'água (levemente inclinado, condensado). Aliança em uma mão. Relógio 2:15 AM. Luz quente. Cama desfeita. 4:5 vertical.",
        format_en="Native long-form image (raw phone photo) | Winner Variation",
        format_pt="Imagem native long-form (foto crua de celular) | Winner Variation",
        execution_en="Copy VERBATIM. Test: Does post-exertion behavior (drinking water) outperform shirt-pull gesture as primary sweat cue? Action vs. display.",
        execution_pt="Copy VERBATIM. Teste: Comportamento pós-esforço (beber água) supera o gesto de puxar a camisa? Ação vs exibição.",
    ),

    # ── ACQ NATIVE IMAGES (Format A) ─────────────
    3: dict(
        title_en="ACQ Native Image: Borrowed Energy (Format A)",
        title_pt="ACQ Native Image: Energia Emprestada (Format A)",
        angle_en="Energy drinks are 'borrowing' from tomorrow — TMC addresses cortisol → T → cellular energy root",
        angle_pt="Energéticos estão 'tomando emprestado' do amanhã — TMC ataca a raiz: cortisol → T → energia celular",
        hookCopy_en='"He was 43, crew chief, couldn\'t get through a morning without three Monsters — and he still crashed by noon."',
        hookCopy_pt='"Ele tinha 43 anos, era chefe de equipe, não conseguia passar a manhã sem três Monsters — e ainda caía ao meio-dia."',
        hookVisual_en="SHOCK CREATIVE (Phone photo): Truck passenger floormat covered in crushed energy drink cans (4-5 cans, crumpled). Interior car lighting, raw, messy. Single element. No text. No staging. [Category: Body Shame / Random Congruence]",
        hookVisual_pt="SHOCK CREATIVE (Foto celular): Tapete do passageiro de caminhão coberto de latas de energético amassadas (4-5 latas). Iluminação interna do carro, crua, bagunçada. Elemento único. Sem texto. [Category: Body Shame / Random Congruence]",
        format_en="Long-form native image (Format A — cold traffic narrative) | Skill: long-form-native-ad-writer",
        format_pt="Native long-form image (Format A — narrativa cold traffic) | Skill: long-form-native-ad-writer",
        speaker_en="Male first-person — Dan, 43, HVAC crew chief",
        speaker_pt="Primeira pessoa masculina — Dan, 43, chefe de equipe HVAC",
        execution_en="HEADLINE: 'I ran an HVAC crew on 4 energy drinks a day for three years. Then my wife left a note on the counter.' | NARRATIVE ~1800w: Cold open in truck at 6:55 AM reaching for second Monster. CHARACTER: Dan, 43, HVAC crew chief. ESCALATION: crashes getting earlier; wife notices body changes; 'maybe tomorrow' to the kids. FAILED SOLUTIONS: energy drinks → pre-workout → coffee → PCP said 'just getting older.' MECHANISM: cortisol suppresses T → T drives ATP/cellular energy → stimulants borrow from tomorrow (adrenal fatigue spiral). DISCOVERY: TMC. TRANSFORMATION week-by-week. BRIDGE. CTA: 365-day guarantee, 40% off.",
        execution_pt="HEADLINE: 'Dirigi uma equipe de HVAC com 4 energéticos por dia por três anos. Depois minha esposa deixou um bilhete na bancada.' | NARRATIVA ~1800w: Abertura no caminhão às 6:55 alcançando o segundo Monster. CHARACTER: Dan, 43. ESCALATION: crashes ficando mais cedo; esposa nota mudanças. MECHANISM: cortisol suprime T → T gera ATP → estimulantes pegam emprestado do amanhã. DISCOVERY: TMC. CTA.",
    ),
    4: dict(
        title_en="ACQ Native Image: The Signal Your Body's Been Sending (Format A)",
        title_pt="ACQ Native Image: O Sinal Que Seu Corpo Vem Enviando (Format A)",
        angle_en="The afternoon energy crash isn't tiredness — it's the loudest testosterone signal a man over 40 can get",
        angle_pt="O crash de energia da tarde não é cansaço — é o sinal de testosterona mais alto que um homem acima dos 40 pode receber",
        hookCopy_en='"His doctor told him his testosterone at 287 was low-normal — nothing we need to treat. Mike still felt like garbage. They were both right, for completely different reasons."',
        hookCopy_pt='"Seu médico disse que testosterona em 287 era normal-baixo — nada que precisasse tratar. Mike ainda se sentia uma merda. Os dois estavam certos, por razões completamente diferentes."',
        hookVisual_en="SHOCK CREATIVE (Phone photo): Printed bloodwork panel — one line circled in red pen: 'Total Testosterone: 287 ng/dL.' Margin note: 'low-normal — no Rx needed.' Single document, close-up, warm desk lamp. [Category: Medical Shock]",
        hookVisual_pt="SHOCK CREATIVE (Foto celular): Painel de exames impresso — uma linha circulada em caneta vermelha: 'Testosterona Total: 287 ng/dL.' Nota na margem: 'normal-baixo — sem receita necessária.' Documento único, close-up. [Category: Medical Shock]",
        format_en="Long-form native image (Format A — cold traffic narrative) | Skill: long-form-native-ad-writer",
        format_pt="Native long-form image (Format A — narrativa cold traffic) | Skill: long-form-native-ad-writer",
        speaker_en="Male first-person — Mike, 48, project manager / desk job",
        speaker_pt="Primeira pessoa masculina — Mike, 48, gerente de projetos",
        execution_en="HEADLINE: 'My doctor said 287 was fine. My wife said I hadn't been present in two years.' | NARRATIVE ~1800w: Mike in doctor's office holding printout. ESCALATION: afternoon crash → productivity dropping → wife noticing. FAILED SOLUTIONS: coffee → pre-workout → TRT consultation. MECHANISM: cortisol peaks afternoon + already-lower T → energy window collapses daily → ashwagandha reduces cortisol → T normalizes. DISCOVERY: TMC. TRANSFORMATION. CTA: 365-day guarantee, 40% off.",
        execution_pt="HEADLINE: 'Meu médico disse que 287 era normal. Minha esposa disse que eu não estava presente há dois anos.' | NARRATIVA ~1800w. MECHANISM: cortisol da tarde + T baixo → janela de energia colapsa. Ashwagandha reduz cortisol → T normaliza. DISCOVERY: TMC. CTA.",
    ),
    15: dict(
        title_en="ACQ Native Image: The Missing Half (Format A)",
        title_pt="ACQ Native Image: A Metade Que Falta (Format A)",
        angle_en="Men spend thousands on protein but ignore the hormonal environment protein synthesis actually requires",
        angle_pt="Homens gastam milhares em proteína mas ignoram o ambiente hormonal que a síntese proteica requer",
        hookCopy_en='"Tom had been lifting since he was 24. At 44, everything was the same — except nothing worked anymore."',
        hookCopy_pt='"Tom levantava peso desde os 24 anos. Aos 44, tudo era igual — exceto que nada funcionava mais."',
        hookVisual_en="SHOCK CREATIVE (Phone photo): Flexed forearm — completely flat. No vascularity, no definition, skin smooth. The absence of what should be there IS the shock. Gym bathroom / fluorescent light. [Category: Body Shame]",
        hookVisual_pt="SHOCK CREATIVE (Foto celular): Antebraço flexionado — completamente plano. Sem veias, sem definição, pele lisa. A ausência do que deveria estar lá É o choque. [Category: Body Shame]",
        format_en="Long-form native image (Format A — cold traffic narrative) | Skill: long-form-native-ad-writer",
        format_pt="Native long-form image (Format A — narrativa cold traffic) | Skill: long-form-native-ad-writer",
        speaker_en="Male first-person — Tom, 44, serious lifter 20 years",
        speaker_pt="Primeira pessoa masculina — Tom, 44, levantador sério por 20 anos",
        execution_en="HEADLINE: 'I spent $3,000 on supplements last year. My body still looked the same. Then I read why.' | NARRATIVE ~1800w: Tom on scale, same number third week. ESCALATION: DOMS lasting 4 days, gains reversing. FAILED SOLUTIONS: more protein → massage gun → ice baths → sports doctor. MECHANISM: recovery requires cortisol clearance; T decline slows clearance → inflammation stays → muscles can't repair. Whey gives building blocks; without hormonal environment, construction crew never shows up. Ashwagandha clears cortisol. DISCOVERY: TMC. TRANSFORMATION. CTA.",
        execution_pt="HEADLINE: 'Gastei $3.000 em suplementos no ano passado. Meu corpo ainda estava igual. Aí eu descobri o porquê.' | NARRATIVA ~1800w. MECHANISM: recuperação exige clearance de cortisol; declínio de T desacelera clearance → inflamação persiste. Ashwagandha limpa cortisol. DISCOVERY: TMC. CTA.",
    ),
    16: dict(
        title_en="ACQ Native Image: The Sunday Morning Test (Format A)",
        title_pt="ACQ Native Image: O Teste da Manhã de Domingo (Format A)",
        angle_en="How a man moves the morning after a workout tells you more about his hormones than any bloodwork",
        angle_pt="Como um homem se move na manhã depois do treino diz mais sobre seus hormônios do que qualquer exame",
        hookCopy_en='"He groaned getting off the couch on a Sunday and my 14-year-old looked at me and said, \'Is Dad okay?\'"',
        hookCopy_pt='"Ele gemeu saindo do sofá num domingo e meu filho de 14 anos me olhou e disse: \'Pai tá bem?\'"',
        hookVisual_en="SHOCK CREATIVE (Phone photo): Pillow with small handwritten note on it: 'Heat pad is on the nightstand.' Wife left this before he woke up. Single element, intimate domestic detail, warm bedroom lighting. [Category: Emotional Devastation]",
        hookVisual_pt="SHOCK CREATIVE (Foto celular): Travesseiro com bilhete escrito à mão: 'Bolsa de calor na mesinha.' Esposa deixou antes dele acordar. Elemento único, detalhe doméstico íntimo. [Category: Emotional Devastation]",
        format_en="Long-form native image (Format A — cold traffic narrative) | Skill: long-form-native-ad-writer",
        format_pt="Native long-form image (Format A — narrativa cold traffic) | Skill: long-form-native-ad-writer",
        speaker_en="Wife/partner POV — Sarah, 44 — story 100% about HIM (LEI #10)",
        speaker_pt="POV esposa — Sarah, 44 — história 100% sobre ELE (LEI #10)",
        execution_en="HEADLINE: 'He used to beat me to the gym on Saturday mornings. Now he lies in bed until 11 on Sundays.' | NARRATIVE ~1800w (wife POV, story 100% about Steve): Steve, 47, weekend warrior. ESCALATION through Sarah's observation: groans louder, workouts shorter, couch becomes recovery room. MECHANISM via Sarah's research: T drops 1%/yr → cortisol clearance slows → DOMS chronic. DISCOVERY: TMC. TRANSFORMATION told through Steve's behavior changes. BRIDGE to wives watching this happen. CTA.",
        execution_pt="HEADLINE: 'Ele costumava chegar antes de mim na academia no sábado. Agora fica na cama até as 11 do domingo.' | NARRATIVA ~1800w (POV esposa, história 100% sobre Steve): MECHANISM: T cai 1%/ano → clearance de cortisol desacelera → DOMS crônica. DISCOVERY: TMC. CTA.",
    ),
    27: dict(
        title_en="ACQ Native Image: The One Variable (Format A)",
        title_pt="ACQ Native Image: A Variável Única (Format A)",
        angle_en="The data-obsessed man quantifies everything except the upstream variable that controls everything else",
        angle_pt="O homem obcecado por dados quantifica tudo menos a variável upstream que controla tudo o mais",
        hookCopy_en='"Jim had a spreadsheet for everything. He was doing everything right. And for two years, nothing changed."',
        hookCopy_pt='"Jim tinha uma planilha pra tudo. Estava fazendo tudo certo. E por dois anos, nada mudou."',
        hookVisual_en="SHOCK CREATIVE (Phone photo): Whoop or Garmin health tracker on wrist, screen showing 'Recovery: 14%' in red. Single wrist, close-up, slightly off-angle. [Category: Medical Shock / Random Congruence]",
        hookVisual_pt="SHOCK CREATIVE (Foto celular): Rastreador de saúde Whoop ou Garmin no pulso, tela mostrando 'Recovery: 14%' em vermelho. Pulso único, close-up. [Category: Medical Shock / Random Congruence]",
        format_en="Long-form native image (Format A — cold traffic narrative) | Skill: long-form-native-ad-writer",
        format_pt="Native long-form image (Format A — narrativa cold traffic) | Skill: long-form-native-ad-writer",
        speaker_en="Male first-person, Urban/Analytical — Jim, 43, software engineer",
        speaker_pt="Primeira pessoa masculina, Urbano/Analítico — Jim, 43, engenheiro de software",
        execution_en="HEADLINE: 'I tracked everything. HRV, macros, sleep stages, VO2 max. My testosterone was 311 and I never thought to measure it.' | NARRATIVE ~1800w: Jim staring at Whoop, HRV at 22. ESCALATION: plateau despite perfect compliance. FAILED SOLUTIONS: creatine → NMN → ashwagandha (wrong dose). MECHANISM: testosterone is the upstream variable controlling all Jim's tracked metrics. Total T: 311. Fix T → all metrics move. Ashwagandha + tongkat ali + boron. DISCOVERY: TMC. TRANSFORMATION in metric language. BRIDGE. CTA.",
        execution_pt="HEADLINE: 'Rastreei tudo. HRV, macros, estágios do sono, VO2 máx. Minha testosterona estava em 311 e nunca pensei em medir.' | NARRATIVA ~1800w. MECHANISM: testosterona é a variável upstream que controla todas as métricas. Total T: 311. Consertar T → todas as métricas melhoram. DISCOVERY: TMC. CTA.",
    ),
    28: dict(
        title_en="ACQ Native Image: The Program That Stopped Working (Format A)",
        title_pt="ACQ Native Image: O Programa Que Parou de Funcionar (Format A)",
        angle_en="Gym programs designed for 25-year-olds are actively working against men over 45",
        angle_pt="Programas de academia projetados para homens de 25 anos trabalham ativamente contra homens acima dos 45",
        hookCopy_en='"Mark had been lifting the same weights for two years. Not because he wasn\'t working hard. Because his body had quietly stopped responding."',
        hookCopy_pt='"Mark levantava os mesmos pesos há dois anos. Não porque não estava se esforçando. Porque seu corpo tinha silenciosamente parado de responder."',
        hookVisual_en="SHOCK CREATIVE (Phone photo): Workout log notebook open — sets, reps, weights in columns, same weight number repeating across 8 consecutive weeks with no increases. Man's stalled progress in his own handwriting. [Category: Body Shame / Emotional Devastation]",
        hookVisual_pt="SHOCK CREATIVE (Foto celular): Caderno de treino aberto — séries, repetições, cargas em colunas, mesmo número repetindo por 8 semanas consecutivas sem aumentos. Progresso travado na própria caligrafia. [Category: Body Shame / Emotional Devastation]",
        format_en="Long-form native image (Format A — cold traffic narrative) | Skill: long-form-native-ad-writer",
        format_pt="Native long-form image (Format A — narrativa cold traffic) | Skill: long-form-native-ad-writer",
        speaker_en="Male first-person — Mark, 46, gym regular 20+ years",
        speaker_pt="Primeira pessoa masculina — Mark, 46, frequentador de academia por 20+ anos",
        execution_en="HEADLINE: 'I've been going to the gym for 22 years. At 46, it stopped working. I finally found out why.' | NARRATIVE ~1800w: Mark in gym bathroom, same number for months. ESCALATION: gains reversed, can't recover, ego bruised. FAILED SOLUTIONS: multiple programs → more protein → TRT consultation (decided against). MECHANISM: standard programs assume T of 600-700+ (25-year-old's environment). Mark's T is 340. Without T to drive synthesis and recovery, progressive overload has no raw material. DISCOVERY: TMC. TRANSFORMATION. BRIDGE. CTA.",
        execution_pt="HEADLINE: 'Frequento academia há 22 anos. Aos 46, parou de funcionar. Finalmente descobri o porquê.' | NARRATIVA ~1800w. MECHANISM: programas padrão assumem T de 600-700+. T de Mark é 340. Sem T, a sobrecarga progressiva não tem matéria-prima. DISCOVERY: TMC. CTA.",
    ),
    39: dict(
        title_en="ACQ Native Image: The Flat Arm (Format A)",
        title_pt="ACQ Native Image: O Braço Murcho (Format A)",
        angle_en="The lost pump isn't vanity — it's a blood flow signal your cardiovascular system sends every workout",
        angle_pt="O pump perdido não é vaidade — é um sinal de fluxo sanguíneo que seu sistema cardiovascular envia a cada treino",
        hookCopy_en='"Gary used to get pumps that made guys in the gym stop and stare. At 52, he flexed and saw nothing."',
        hookCopy_pt='"Gary costumava ter pumps que faziam os caras na academia pararem para olhar. Aos 52, ele flexionava e não via nada."',
        hookVisual_en="SHOCK CREATIVE (Phone photo): Flexed forearm — completely flat. No veins, no definition, skin smooth. The absence of the expected pump IS the shock. Gym bathroom / fluorescent light. Single body part, close-up. [Category: Body Shame]",
        hookVisual_pt="SHOCK CREATIVE (Foto celular): Antebraço flexionado — completamente murcho. Sem veias, sem definição. A ausência do pump esperado É o choque. [Category: Body Shame]",
        format_en="Long-form native image (Format A — cold traffic narrative) | Skill: long-form-native-ad-writer",
        format_pt="Native long-form image (Format A — narrativa cold traffic) | Skill: long-form-native-ad-writer",
        speaker_en="Male first-person — Gary, 52, serious lifter 25 years",
        speaker_pt="Primeira pessoa masculina — Gary, 52, levantador sério por 25 anos",
        execution_en="HEADLINE: 'I used to get veins from my wrist to my shoulder. At 52, I flex and nothing happens. I finally found out why.' | NARRATIVE ~1800w: Gary in gym bathroom mid-workout, flexing — flat. ESCALATION: pump smaller every year; workouts feel hollow; motivation declining. FAILED SOLUTIONS: pre-workout → L-citrulline alone → arginine. MECHANISM: NO pathway requires eNOS activity driven by T; as T declines, even L-citrulline is compromised. TMC: L-citrulline (NO) + tongkat ali (T → eNOS). DISCOVERY. TRANSFORMATION. BRIDGE. CTA.",
        execution_pt="HEADLINE: 'Tinha veias do pulso ao ombro. Aos 52, flexiono e nada acontece. Finalmente descobri o porquê.' | NARRATIVA ~1800w. MECHANISM: via NO requer atividade eNOS impulsionada por T; declínio de T compromete até o L-citrulline. TMC: L-citrulline + tongkat ali. DISCOVERY: TMC. CTA.",
    ),
    40: dict(
        title_en="ACQ Native Image: The 98% Problem (Format A)",
        title_pt="ACQ Native Image: O Problema dos 98% (Format A)",
        angle_en="Most men with 'normal' testosterone still feel terrible — because 98% of their T is biologically unavailable",
        angle_pt="A maioria dos homens com testosterona 'normal' ainda se sente péssima — porque 98% do T deles é biologicamente indisponível",
        hookCopy_en='"Bob\'s doctor told him his testosterone was in the normal range. Bob still felt like garbage. They were both right — for completely different reasons."',
        hookCopy_pt='"O médico disse que a testosterona de Bob estava na faixa normal. Bob ainda se sentia uma merda. Os dois estavam certos — por razões completamente diferentes."',
        hookVisual_en="SHOCK CREATIVE (Phone photo): Printed lab panel — two highlighted lines: 'Total Testosterone: 512 ng/dL (Normal ✓)' and below it 'Free Testosterone: 4.1 pg/mL (LOW ↓)'. The contrast between Normal and LOW in the same printout IS the shock. [Category: Medical Shock]",
        hookVisual_pt="SHOCK CREATIVE (Foto celular): Resultado de exame impresso — duas linhas destacadas: 'Testosterona Total: 512 ng/dL (Normal ✓)' e abaixo 'Testosterona Livre: 4.1 pg/mL (BAIXA ↓)'. O contraste entre Normal e BAIXO no mesmo laudo É o choque. [Category: Medical Shock]",
        format_en="Long-form native image (Format A — cold traffic narrative) | Skill: long-form-native-ad-writer",
        format_pt="Native long-form image (Format A — narrativa cold traffic) | Skill: long-form-native-ad-writer",
        speaker_en="Male first-person — Bob, 54, frustrated after being told T is 'fine'",
        speaker_pt="Primeira pessoa masculina — Bob, 54, frustrado após ser dito que T está 'normal'",
        execution_en="HEADLINE: 'My doctor said my testosterone was normal. Then I learned about the protein that was stealing 98% of it.' | NARRATIVE ~1800w: Bob in doctor's office, Total T 512, 'that's normal Bob.' ESCALATION: every symptom of low T despite 'normal' results. FAILED SOLUTIONS: TRT wouldn't prescribe → supplements → one naturopath who mentioned SHBG briefly. MECHANISM: SHBG binds 98% of T → Free T 4.1 pg/mL (critical low) → Boron 10mg reduces SHBG → free T rises → body can actually use it. DISCOVERY: TMC (boron + tongkat ali + ashwagandha). TRANSFORMATION (labs that finally change). BRIDGE to men told they're 'normal' but feel otherwise. CTA.",
        execution_pt="HEADLINE: 'Meu médico disse que minha testosterona estava normal. Depois aprendi sobre a proteína que roubava 98% dela.' | NARRATIVA ~1800w. MECHANISM: SHBG liga 98% do T → T Livre 4.1 pg/mL → Boro 10mg reduz SHBG → T Livre sobe. DISCOVERY: TMC. CTA.",
    ),
    51: dict(
        title_en="ACQ Native Image: What Cortisol Does to Your Brain (Format A)",
        title_pt="ACQ Native Image: O Que o Cortisol Faz ao Seu Cérebro (Format A)",
        angle_en="Brain fog in men over 40 isn't mental — it's a cortisol-BDNF-hippocampus cascade with a specific fix",
        angle_pt="Brain fog em homens acima dos 40 não é mental — é uma cascata cortisol-BDNF-hipocampo com uma solução específica",
        hookCopy_en='"Paul built his career on thinking fast. At 49, he started losing words mid-sentence in front of his team. His doctor had three words for him: It\'s just stress."',
        hookCopy_pt='"Paul construiu sua carreira pensando rápido. Aos 49, começou a perder palavras no meio de frases na frente da equipe. Seu médico tinha três palavras: É só estresse."',
        hookVisual_en="SHOCK CREATIVE (Phone photo): Laptop screen with half-written email — cursor blinking mid-sentence, text cuts off: 'I wanted to follow up on the...' and stops. Photographed in the moment of forgetting. Single element. [Category: Emotional Devastation / Random Congruence]",
        hookVisual_pt="SHOCK CREATIVE (Foto celular): Tela de laptop com e-mail pela metade — cursor piscando no meio da frase, texto para: 'Queria dar um retorno sobre o...' e nada. Fotografado no momento do esquecimento. Elemento único. [Category: Emotional Devastation / Random Congruence]",
        format_en="Long-form native image (Format A — cold traffic narrative) | Skill: long-form-native-ad-writer",
        format_pt="Native long-form image (Format A — narrativa cold traffic) | Skill: long-form-native-ad-writer",
        speaker_en="Male first-person, Urban/Analytical — Paul, 49, VP engineering",
        speaker_pt="Primeira pessoa masculina, Urbano/Analítico — Paul, 49, VP de Engenharia",
        execution_en="HEADLINE: 'I'm a VP of engineering. At 49, I started losing words mid-sentence in meetings. My doctor said I was just stressed.' | NARRATIVE ~1800w: Paul mid-presentation, loses word 'infrastructure.' ESCALATION: re-reads emails 3x; forgets vendor names; 12-year-old's logic becomes hard to follow. FAILED SOLUTIONS: sleep hygiene → cutting caffeine → neurologist → psychiatrist. MECHANISM: chronic cortisol suppresses BDNF → synaptic plasticity declines → word retrieval fails → hippocampus literally shrinks under chronic cortisol. Ashwagandha → cortisol ↓ → BDNF recovers. Lion's Mane → NGF → neuroplasticity. DISCOVERY: TMC. TRANSFORMATION. BRIDGE. CTA.",
        execution_pt="HEADLINE: 'Sou VP de engenharia. Aos 49, comecei a perder palavras no meio de frases nas reuniões. Meu médico disse que era só estresse.' | NARRATIVA ~1800w. MECHANISM: cortisol crônico suprime BDNF → plasticidade sináptica declina → hipocampo encolhe literalmente. Ashwagandha → cortisol ↓ → BDNF se recupera. Lion's Mane → NGF. DISCOVERY: TMC. CTA.",
    ),
    52: dict(
        title_en="ACQ Native Image: The 47 Things (Format A)",
        title_pt="ACQ Native Image: As 47 Coisas (Format A)",
        angle_en="Brain fog isn't a feeling — it's behavioral: the closet, the email, the project you can't start",
        angle_pt="Brain fog não é uma sensação — é comportamental: o armário, o e-mail, o projeto que você não consegue começar",
        hookCopy_en='"Richard wasn\'t lazy. He wasn\'t depressed. He knew exactly what needed to be done. He just couldn\'t make himself start any of it."',
        hookCopy_pt='"Richard não era preguiçoso. Não estava deprimido. Sabia exatamente o que precisava ser feito. Simplesmente não conseguia se forçar a começar nada."',
        hookVisual_en="SHOCK CREATIVE (Phone photo): Open notebook with handwritten to-do list — last item stopping mid-word: 'Call back' and then nothing. Like the pen just stopped. Single element. Warm desk lamp light. [Category: Emotional Devastation]",
        hookVisual_pt="SHOCK CREATIVE (Foto celular): Caderno aberto com lista de tarefas escrita à mão — último item parando no meio da palavra: 'Ligar de' e nada. Como se a caneta tivesse simplesmente parado. Elemento único. Luz de mesa quente. [Category: Emotional Devastation]",
        format_en="Long-form native image (Format A — cold traffic narrative) | Skill: long-form-native-ad-writer",
        format_pt="Native long-form image (Format A — narrativa cold traffic) | Skill: long-form-native-ad-writer",
        speaker_en="Male first-person — Richard, 51, overwhelmed professional",
        speaker_pt="Primeira pessoa masculina — Richard, 51, profissional sobrecarregado",
        execution_en="HEADLINE: 'I have the list. I have the time. I sit down to start, and nothing happens. I'm not depressed. I don't know what I am.' | NARRATIVE ~1800w: Richard at home office desk 9 AM Saturday, list in front of him. Three hours later — nothing done. ESCALATION: inability-to-start spreads across domains; Googled 'executive dysfunction' at 2 AM. FAILED SOLUTIONS: therapy → caffeine cycles → Adderall (made anxiety worse). MECHANISM: chronic cortisol impairs prefrontal cortex → executive function fails: initiation, task-switching, inhibition of distraction. 'Can't start' is cortisol-driven neurological event. Ashwagandha → cortisol ↓ → PFC function recovers. Lion's Mane → NGF → dopamine signaling. DISCOVERY: TMC. TRANSFORMATION (Saturday through the list, start to finish). BRIDGE. CTA.",
        execution_pt="HEADLINE: 'Tenho a lista. Tenho o tempo. Sento para começar, e nada acontece. Não estou deprimido. Não sei o que sou.' | NARRATIVA ~1800w. MECHANISM: cortisol crônico prejudica o córtex pré-frontal → função executiva falha: iniciação, alternância de tarefas. 'Não consegue começar' é evento neurológico induzido por cortisol. Ashwagandha → cortisol ↓ → PFC se recupera. Lion's Mane → NGF → dopamina. DISCOVERY: TMC. CTA.",
    ),
}

# ─────────────────────────────────────────────────
# PATCH FUNCTION
# ─────────────────────────────────────────────────
def escape_js(s):
    """Escape for JS string (double-quote delimited)."""
    return s.replace('\\', '\\\\').replace('"', '\\"').replace('\n', ' ')

def patch_field(js_block, field, new_value):
    """Replace field:\"...\", pattern in a JS object string."""
    pattern = rf'{re.escape(field)}:"[^"]*(?:\\.[^"]*)*"'
    replacement = f'{field}:"{escape_js(new_value)}"'
    result, n = re.subn(pattern, replacement, js_block)
    if n == 0:
        print(f"  WARNING: field '{field}' not found in block")
    return result

# Extract ADS array bounds
ads_start = html.find('const ADS = [')
ads_end = html.find('];', ads_start) + 2
ads_js = html[ads_start:ads_end]

# Split into individual ad objects
# Each ad starts with {id:N,
ad_objects = []
pattern = re.compile(r'(\{id:(\d+),.*?\})', re.DOTALL)
for m in pattern.finditer(ads_js):
    ad_objects.append((m.start(), m.end(), int(m.group(2)), m.group(1)))

patched_ads_js = ads_js
offset = 0

for orig_start, orig_end, ad_id, orig_block in ad_objects:
    if ad_id not in UPDATES:
        continue

    print(f"Patching ad id={ad_id}...")
    new_block = orig_block
    for field, value in UPDATES[ad_id].items():
        new_block = patch_field(new_block, field, value)

    # Replace in patched string (adjust for offset)
    abs_start = orig_start + offset
    abs_end = orig_end + offset
    patched_ads_js = patched_ads_js[:abs_start] + new_block + patched_ads_js[abs_end:]
    offset += len(new_block) - (orig_end - orig_start)

# Reconstruct full HTML
new_html = html[:ads_start] + patched_ads_js + html[ads_end:]

# Update content-version marker so curl check works
import datetime
today = datetime.date.today().strftime('%Y-%m-%d')
new_html = re.sub(
    r'content-version["\s:]+["\']?[^"\'<\s]+',
    f'content-version: "B14-corrected-{today}"',
    new_html,
    count=1
)

HTML_PATH.write_text(new_html)
print(f"\n✅ Done. {len(UPDATES)} ads patched. HTML written to {HTML_PATH}")
print(f"   Content-version: B14-corrected-{today}")
