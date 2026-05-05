#!/usr/bin/env python3
"""
Update B14 review (v2) — apply 32 ad corrections from review feedback 2026-05-05.

Categories of correction:
- 15 ads → New concept in AI Animated Pixar-Style (Cortisol vilão, Testosterone, Dopamine, BDNF, Vein, Brain personagens)
- 3 ads → Keep approved hook, change format to Pixar-Style
- 6 ads → Native long-form rewrites (intimate/embarrassing personal stories)
- 6 ads → Specific corrections (text fix, format change, hook expansion, no Google Trends)
- 2 ads → Total rewrites

Approved-untouched ads (10): #5, #6, #7, #8, #17, #19, #20, #23, #45, #47 — NOT modified.

Per-ad versioning: each modified ad gets `v:2` field. loadState() drops state entries
whose version doesn't match — modified ads return to "pending", unmodified stay approved.
"""

import re
import datetime
from pathlib import Path

HTML_PATH = Path("/tmp/tmc-ads-review/index.html")
html = HTML_PATH.read_text()

TODAY = datetime.date.today().strftime('%Y-%m-%d')
VERSION_TAG = f"B14-corrected-v2-{TODAY}"

# ═══════════════════════════════════════════════════════════════
# UPDATES — only fields that change for each ad
# ═══════════════════════════════════════════════════════════════

UPDATES = {

    # ──────────────────────────────────────────────────
    # SEGUNDA — C2 / ENERGY CRASH
    # ──────────────────────────────────────────────────

    # AD #9 — TMCAD-183 — New Pixar concept: Cortisol vilão personagem
    9: dict(
        angle_en="Cortisol personified as Pixar-style villain hijacking testosterone — cross-cluster bridge via animated character",
        angle_pt="Cortisol personificado como vilão Pixar sequestrando a testosterona — bridge cross-cluster via personagem animado",
        hookCopy_en="\"Hi, I'm cortisol — and at 3pm, I'm the reason your energy disappears.\"",
        hookCopy_pt="\"Oi, eu sou seu cortisol — e às 3 da tarde, eu sou o motivo da sua energia desaparecer.\"",
        hookVisual_en="VISUAL HOOK (AI Animated 3D Pixar-Style): Cortisol villain — yellow/oxidized viscous creature — appears inside the body (interior view, Inside Out style), grabbing testosterone molecules and tossing them aside one by one. Turns to camera with malicious grin.",
        hookVisual_pt="VISUAL HOOK (Animação 3D AI Pixar-Style): Cortisol vilão — criatura amarela/oxidada e viscosa — aparece dentro do corpo (vista interna, estilo Inside Out), pegando moléculas de testosterona e jogando uma por uma de lado. Vira pra câmera com sorriso malicioso.",
        format_en="AI Animated Pixar-Style 3D | Validated internally (TMCAD72, TMCAD01 B9 HK1)",
        format_pt="Animação 3D AI Pixar-Style | Validado internamente (TMCAD72, TMCAD01 B9 HK1)",
        speaker_en="Cortisol personified (Pixar 3D character) — yellow oxidized villain that lives inside the body",
        speaker_pt="Cortisol personificado (personagem Pixar 3D) — vilão amarelo oxidado que vive dentro do corpo",
        execution_en="DURATION 75s. Structure: \"Hi, I'm your [X]\" validated in Pixar ads. Cortisol (animated villain) introduces himself directly to viewer, explains how he steals testosterone every afternoon. Brief mechanism (cortisol suppresses T → energy crash). TMC reveal: ashwagandha shuts down cortisol. CTA with 'they'll' (animated mascot pronoun, LEI #4). Speaker IMPREVISÍVEL + congruente (cortisol = energy crash). Point-of-pain SPECIFIC (3pm energy disappears).",
        execution_pt="DURAÇÃO 75s. Estrutura: \"Oi, eu sou seu [X]\" validada em ads Pixar. Cortisol (vilão animado) se apresenta diretamente ao espectador, explica como ele rouba testosterona toda tarde. Mecanismo breve (cortisol suprime T → energy crash). Revela TMC: ashwagandha desliga cortisol. CTA com 'they'll' (mascote animado, LEI #4). Speaker IMPREVISÍVEL + congruente (cortisol = energy crash). Point-of-pain ESPECÍFICO (3pm energia some).",
    ),

    # AD #10 — TMCAD-184 — New Pixar LONG: Cortisol vilão Mini-VSL
    10: dict(
        angle_en="Cortisol Pixar villain runs the body's control room — Mini-VSL exploring 3 symptoms (energy/recovery/focus) sabotaged by 1 hormone",
        angle_pt="Cortisol vilão Pixar comanda a sala de controle do corpo — Mini-VSL explorando 3 sintomas (energia/recovery/foco) sabotados por 1 hormônio",
        hookCopy_en="\"Meet cortisol. He's been running your body since you turned 40. And he's terrible at it.\"",
        hookCopy_pt="\"Conheça o cortisol. Ele tá comandando seu corpo desde que você fez 40. E ele é péssimo nisso.\"",
        hookVisual_en="VISUAL HOOK (AI Animated 3D Pixar-Style): Cortisol villain enters the body's control room (central brain HQ, Inside Out style). Begins sabotaging 3 control panels simultaneously: ENERGY / RECOVERY / FOCUS. Other hormones (T, dopamine) tied up in corners.",
        hookVisual_pt="VISUAL HOOK (Animação 3D AI Pixar-Style): Cortisol vilão entra na sala de controle do corpo (HQ central no cérebro, estilo Inside Out). Começa a sabotar 3 painéis simultaneamente: ENERGIA / RECOVERY / FOCO. Outros hormônios (T, dopamina) amarrados nos cantos.",
        format_en="AI Animated Pixar-Style 3D — Mini-VSL narrative (3:30)",
        format_pt="Animação 3D AI Pixar-Style — Mini-VSL narrativo (3:30)",
        speaker_en="Cortisol villain (continuity from AD#9) — now in Mini-VSL storytelling format with full cast (T, Dopamine, BDNF visible as bound prisoners)",
        speaker_pt="Cortisol vilão (continuity do AD#9) — agora em formato Mini-VSL storytelling com elenco completo (T, Dopamina, BDNF visíveis como prisioneiros)",
        execution_en="DURATION 3:30 (Pixar works best <4min). Cross-cluster bridge (1 hormone, 3 symptoms) executed via epic Pixar storytelling. Cortisol narrates his takeover with sarcastic humor (Mr. Burns vibe). Shows cascading damage to energy/recovery/focus. Then heroes arrive: ashwagandha (suit-wearing fixer), tongkat ali, Lion's Mane. They liberate the control room. CTA with 'they'll' (mascot, LEI #4). Entertainment-first DR. Cumpre 'ad inteiro nativamente curioso'.",
        execution_pt="DURAÇÃO 3:30 (Pixar funciona melhor <4min). Bridge cross-cluster (1 hormônio, 3 sintomas) executado via storytelling Pixar épico. Cortisol narra sua tomada de poder com humor sarcástico (vibe Mr. Burns). Mostra dano em cascata em energia/recovery/foco. Heróis chegam: ashwagandha (consertador de terno), tongkat ali, Lion's Mane. Eles libertam a sala de controle. CTA com 'they'll' (mascote, LEI #4).",
    ),

    # AD #11 — TMCRMKT-30 — Hook B fix: 218 points / 38 days
    11: dict(
        hookCopy_en="HOOK A: \"I thought TMC was just overpriced coffee. I was wrong. Here's what's actually happening in your body.\"  ||  HOOK B (UPDATED per Derick): \"Think TMC is just coffee? Then explain why my testosterone went up 218 points in 38 days.\"  ||  HOOK C: \"My buddy called TMC 'expensive dirt water.' 3 months later, he ordered his own.\"",
        hookCopy_pt="HOOK A: \"Achei que TMC era só café caro. Estava errado. Aqui está o que realmente acontece no seu corpo.\"  ||  HOOK B (ATUALIZADO por Derick): \"Acha que TMC é só café? Então explica por que minha testosterona subiu 218 pontos em 38 dias.\"  ||  HOOK C: \"Meu amigo chamou TMC de 'água com terra cara.' 3 meses depois, ele pediu o dele.\"",
        execution_en="DURATION 90s. Hook B updated per Derick feedback: 200→218 (broken numbers more credible) + 90 days→38 days (faster result more shocking). Speaker admits skepticism, explains: 'Regular coffee = caffeine. TMC = ashwagandha (cortisol reduction), tongkat ali (T-support), Lion's Mane (brain function) — clinical doses.' Brief mechanism per ingredient. Personal result (218 pts in 38 days). CTA with 'they'll'.",
        execution_pt="DURAÇÃO 90s. Hook B atualizado conforme feedback do Derick: 200→218 (números quebrados mais críveis) + 90 dias→38 dias (resultado mais rápido = mais chocante). Speaker admite ceticismo, explica: 'Café comum = cafeína. TMC = ashwagandha (redução cortisol), tongkat ali (suporte T), Lion's Mane (função cerebral) — doses clínicas.' Mecanismo breve por ingrediente. Resultado pessoal (218 pts em 38 dias). CTA com 'they'll'.",
    ),

    # ──────────────────────────────────────────────────
    # TERÇA — C2 / ALWAYS SORE
    # ──────────────────────────────────────────────────

    # AD #18 — TMCAD-188 — New Pixar: Bicep falante exausto
    18: dict(
        angle_en="Personified bicep (Pixar-style 3D) confronts viewer about hormonal neglect — recovery cluster mapped to character",
        angle_pt="Bíceps personificado (Pixar 3D) confronta espectador sobre negligência hormonal — cluster recovery mapeado para personagem",
        hookCopy_en="\"Hi, I'm your muscle — and I'm exhausted because you've been ignoring my hormones for 10 years.\"",
        hookCopy_pt="\"Oi, eu sou seu músculo — e eu tô exausto porque você tem ignorado meus hormônios há 10 anos.\"",
        hookVisual_en="VISUAL HOOK (AI Animated 3D Pixar-Style): Animated bicep — sweaty, slumped, defeated — tries to lift a tiny dumbbell, fails, throws it on the ground and yells: \"I QUIT!\" Camera dolly out reveals other muscle groups equally fatigued.",
        hookVisual_pt="VISUAL HOOK (Animação 3D AI Pixar-Style): Bíceps animado — suado, encurvado, derrotado — tenta levantar uma haltera minúscula, falha, joga no chão e grita: \"EU DESISTO!\" Câmera dolly out revela outros grupos musculares igualmente fatigados.",
        format_en="AI Animated Pixar-Style 3D | Validated internally",
        format_pt="Animação 3D AI Pixar-Style | Validado internamente",
        speaker_en="Bicep personified (Pixar 3D character) — exhausted, sweaty, defeated muscle",
        speaker_pt="Bíceps personificado (personagem Pixar 3D) — músculo exausto, suado, derrotado",
        execution_en="DURATION 75s. Structure: \"Hi, I'm your [X]\" validated. Bicep explains via metaphor: he needs hormones (T, less cortisol) to do his job. Without them, recovery fails, soreness lingers. TMC fixes the hormonal foundation. Speaker IMPREVISÍVEL + congruente (muscle = recovery cluster). Point-of-pain SPECIFIC (can't recover after workouts). CTA with 'they'll'.",
        execution_pt="DURAÇÃO 75s. Estrutura: \"Oi, eu sou seu [X]\" validada. Bíceps explica via metáfora: ele precisa de hormônios (T, menos cortisol) pra fazer o trabalho. Sem eles, recovery falha, soreness persiste. TMC consegue a foundation hormonal. Speaker IMPREVISÍVEL + congruente (músculo = cluster recovery). Point-of-pain ESPECÍFICO (não consegue recuperar). CTA com 'they'll'.",
    ),

    # AD #21 — TMCAD-191 — New Pixar: Testosterona personagem (encolhe ao vivo)
    21: dict(
        angle_en="Personified testosterone shrinks LIVE during hook — visualizing T-decline as character transformation",
        angle_pt="Testosterona personificada encolhe AO VIVO durante o hook — visualizando T-decline como transformação de personagem",
        hookCopy_en="\"Hi, I'm your testosterone — and here's why I've been getting weaker since you turned 40.\"",
        hookCopy_pt="\"Oi, eu sou sua testosterona — e aqui está o motivo de eu estar ficando mais fraca desde que você fez 40.\"",
        hookVisual_en="VISUAL HOOK (AI Animated 3D Pixar-Style): Testosterone personified — starts \"young and powerful\" (25yo version, muscular, glowing). During first 3s of hook, T VISIBLY SHRINKS in front of viewer, losing brightness, muscle, height. Ends as smaller weaker version (45yo). Transformation = imprevisibility extreme + WTF effect.",
        hookVisual_pt="VISUAL HOOK (Animação 3D AI Pixar-Style): Testosterona personificada — começa \"jovem e poderosa\" (versão 25 anos, musculosa, brilhante). Durante primeiros 3s do hook, T ENCOLHE VISIVELMENTE na frente do espectador, perdendo brilho, músculo, altura. Termina como versão menor e mais fraca (45 anos). Transformação = imprevisibilidade extrema + efeito WTF.",
        format_en="AI Animated Pixar-Style 3D | Validated internally",
        format_pt="Animação 3D AI Pixar-Style | Validado internamente",
        speaker_en="Testosterone personified (Pixar 3D character) — undergoes live shrinking transformation in hook",
        speaker_pt="Testosterona personificada (personagem Pixar 3D) — sofre transformação encolhendo ao vivo no hook",
        execution_en="DURATION 2:40. Structure: \"Hi, I'm your [X]\" + visual transformation. T explains the cascade: SHBG traps her, cortisol suppresses production, dopamine signaling weakens. \"You're not weaker. I am.\" TMC ingredients (boron frees SHBG, tongkat ali boosts production, ashwagandha cuts cortisol) appear as Pixar heroes restoring T to glory at end. Speaker IMPREVISÍVEL (T encolhendo ao vivo), congruente (cluster muscle/recovery). CTA with 'they'll'.",
        execution_pt="DURAÇÃO 2:40. Estrutura: \"Oi, eu sou sua [X]\" + transformação visual. T explica a cascata: SHBG aprisiona ela, cortisol suprime produção, sinalização dopamina enfraquece. \"Você não está mais fraco. Eu estou.\" Ingredientes TMC (boron libera SHBG, tongkat ali aumenta produção, ashwagandha corta cortisol) aparecem como heróis Pixar restaurando T à glória no final. Speaker IMPREVISÍVEL (T encolhendo ao vivo), congruente. CTA com 'they'll'.",
    ),

    # AD #22 — TMCAD-192 — New Pixar LONG: Reino caído épico
    22: dict(
        angle_en="Mini-VSL Pixar — fallen kingdom inside the body, T as overthrown ruler, ingredients as resistance heroes",
        angle_pt="Mini-VSL Pixar — reino caído dentro do corpo, T como governante destronado, ingredientes como heróis da resistência",
        hookCopy_en="\"There used to be a kingdom inside you that ran your gym. It's been overthrown. Let me tell you the story.\"",
        hookCopy_pt="\"Existia um reino dentro de você que comandava sua academia. Ele foi derrubado. Deixa eu te contar a história.\"",
        hookVisual_en="VISUAL HOOK (AI Animated 3D Pixar-Style): Epic city inside the body. T as deposed mayor, exiled. Cortisol invades wearing villain crown. SHBG locks T in a castle. Dopamine cries in a corner. Aerial shot of decaying kingdom = stylized Pixar opening worthy of feature film.",
        hookVisual_pt="VISUAL HOOK (Animação 3D AI Pixar-Style): Cidade épica dentro do corpo. T como prefeito deposto, exilado. Cortisol invade usando coroa de vilão. SHBG tranca T num castelo. Dopamina chora num canto. Plano aéreo do reino em decadência = abertura Pixar estilizada digna de longa-metragem.",
        format_en="AI Animated Pixar-Style 3D — Mini-VSL épico (3:30)",
        format_pt="Animação 3D AI Pixar-Style — Mini-VSL épico (3:30)",
        speaker_en="Cast of personified hormones (Pixar 3D) — T (fallen hero), Cortisol (villain), SHBG (jailer), Boron (liberator), Tongkat Ali (general), Ashwagandha (advisor)",
        speaker_pt="Elenco de hormônios personificados (Pixar 3D) — T (herói caído), Cortisol (vilão), SHBG (carcereiro), Boron (libertador), Tongkat Ali (general), Ashwagandha (conselheira)",
        execution_en="DURATION 3:30. Mini-VSL épico Pixar. Mechanism (T-decline cascade) becomes visual narrative. Resistance forms — TMC ingredients arrive as heroes one by one, retake the kingdom. Pure entertainment + education. Cumpre voice-criteria 'ad inteiramente curioso'. CTA with 'they'll'.",
        execution_pt="DURAÇÃO 3:30. Mini-VSL Pixar épico. Mecanismo (cascata T-decline) vira narrativa visual. Resistência se forma — ingredientes TMC chegam como heróis um por um, retomam o reino. Entretenimento puro + educação. Cumpre voice-criteria 'ad inteiramente curioso'. CTA com 'they'll'.",
    ),

    # AD #24 — TMCRMKTI-24 — RTG Image: Whey vs TMC (cost-pain split)
    24: dict(
        angle_en="Reframe protein-only post-workout behavior — without T to drive synthesis, expensive whey is wasted",
        angle_pt="Reframe do comportamento de só usar whey pós-treino — sem T pra dirigir síntese, whey caro é desperdiçado",
        hookCopy_en="HEADLINE: \"Stop wasting your post-workout protein.\" SUBHEAD: \"Without testosterone to drive synthesis, your $200/month whey is useless. TMC fixes the foundation.\"",
        hookCopy_pt="HEADLINE: \"Pare de desperdiçar sua proteína pós-treino.\" SUBHEAD: \"Sem testosterona pra dirigir a síntese, seu whey de $200/mês é inútil. TMC consegue a foundation.\"",
        hookVisual_en="VISUAL: Split-screen 4:5 vertical Meta — LEFT: giant whey tub with \"$ thrown away\" overlay, semi-faded. RIGHT: TMC cup centered, vivid colors, \"$2/day\" callout. Clean modern design. Trust badges (guarantee, ingredient count) at bottom.",
        hookVisual_pt="VISUAL: Split-screen 4:5 vertical Meta — ESQUERDA: balde de whey gigante com overlay \"$ jogado fora\", semi-desbotado. DIREITA: cup TMC centralizada, cores vivas, callout \"$2/dia\". Design clean moderno. Selos de confiança no rodapé.",
        format_en="RTG Static Image (4:5 vertical, Format B — Bold/Comparison) | Skill: long-form-native-ad-writer or design",
        format_pt="RTG Static Image (4:5 vertical, Format B — Bold/Comparação) | Skill: long-form-native-ad-writer ou design",
        speaker_en="N/A (static image, brand-direct copy)",
        speaker_pt="N/A (imagem estática, copy direto da marca)",
        execution_en="DURATION N/A. Per Derick feedback: hit on 'using protein after workout instead of TMC'. Cost-pain hook (Life Cykel pattern, validated). Reframe: protein alone incomplete without hormonal foundation. CTA: 'TMC fixes what whey alone can't → 365-day risk-free, 40% off + free shipping' (LEI #4).",
        execution_pt="DURAÇÃO N/A. Conforme feedback do Derick: bate na ideia de 'usar proteína depois do treino, ao invés de TMC'. Cost-pain hook (Life Cykel pattern, validado). Reframe: proteína sozinha incompleta sem foundation hormonal. CTA: 'TMC conserta o que whey sozinho não pode → 365-day risk-free, 40% off + frete grátis' (LEI #4).",
    ),

    # ──────────────────────────────────────────────────
    # QUARTA — C2 / ZERO DRIVE
    # ──────────────────────────────────────────────────

    # AD #27 — TMCIMG-155 — Native rewrite: Lacrosse jersey (intimate)
    27: dict(
        angle_en="Married man's college jersey doesn't fit anymore — anniversary failure as personal/intimate/embarrassing identity collapse",
        angle_pt="Camiseta da faculdade do homem casado não cabe mais — falha de aniversário como colapso de identidade pessoal/íntimo/constrangedor",
        hookCopy_en="\"Mark put on his college jersey, looked in the mirror, and saw a man he didn't recognize. His 19-year-old self stared back from the framed team photo on the wall. Then he took the jersey off and put it back in the box.\"",
        hookCopy_pt="\"Mark vestiu sua camiseta da faculdade, se olhou no espelho, e viu um homem que não reconhecia. Seu eu de 19 anos retribuía o olhar da foto emoldurada do time na parede. Então ele tirou a camiseta e colocou de volta na caixa.\"",
        hookVisual_en="SHOCK CREATIVE (Phone selfie): Mark in front of bedroom mirror, wearing his old college lacrosse jersey (XL, name on back, 1996) — clearly tight across chest and stomach, marking man boobs and gut. Embarrassed posture, head slightly down. Framed team photo from 1996 visible on wall behind him. Single intimate element. [Category: Shame / Identity Loss]",
        hookVisual_pt="SHOCK CREATIVE (Selfie de celular): Mark em frente ao espelho do quarto, vestindo sua antiga camiseta de lacrosse da faculdade (XL, nome nas costas, 1996) — claramente apertada no peito e barriga, marcando man boobs e gut. Postura envergonhada, cabeça levemente baixa. Foto emoldurada do time de 1996 visível na parede atrás. Elemento único íntimo. [Category: Shame / Identity Loss]",
        format_en="Long-form native image (Format A — cold traffic narrative) | Skill: long-form-native-ad-writer",
        format_pt="Native long-form image (Format A — narrativa cold traffic) | Skill: long-form-native-ad-writer",
        speaker_en="Male first-person — Mark, 47, ex-college lacrosse player, 25 years married",
        speaker_pt="Primeira pessoa masculina — Mark, 47, ex-jogador de lacrosse da faculdade, 25 anos casado",
        execution_en="HEADLINE: 'I tried on my old college lacrosse jersey to surprise my wife on our anniversary. I haven't worn it since.' | NARRATIVE ~1800w (intimate/embarrassing tone per Derick feedback): Open in bedroom, anniversary morning. ESCALATION: Mark hides old photos from iPhone; stops going to pool with kids; buys looser shirts; one day, finds the jersey in box from college. Anniversary plan: surprise her in it. Mirror moment is devastating. FAILED SOLUTIONS: military diet → 5x/week gym → expensive personal trainer → doctor said 'scale back at your age'. MECHANISM REVEAL: T dropped from 700+ to 340; without T, body doesn't respond no matter the effort. DISCOVERY: TMC. TRANSFORMATION: the day the jersey fits again. BRIDGE TO READER. CTA (LEI #4).",
        execution_pt="HEADLINE: 'Vesti a camiseta da minha faculdade pra surpreender minha esposa no aniversário. Não vesti de novo desde então.' | NARRATIVA ~1800w (tom íntimo/constrangedor conforme feedback do Derick): Abre no quarto, manhã do aniversário. ESCALATION: Mark esconde fotos antigas do iPhone; para de ir na piscina com filhos; compra camisas mais largas; um dia, encontra a camiseta na caixa da faculdade. Plano: surpreendê-la com ela. Momento do espelho é devastador. FAILED SOLUTIONS: dieta militar → academia 5x → personal caro → médico falou 'maneirar nessa idade'. MECHANISM: T caiu de 700+ pra 340; sem T, corpo não responde por mais que tente. DISCOVERY: TMC. TRANSFORMATION: o dia que a jersey volta a servir. CTA (LEI #4).",
    ),

    # AD #28 — TMCIMG-156 — Native rewrite: Ignored fridge notes (intimate)
    28: dict(
        angle_en="Wife stopped inviting husband to work out — silent intimate failure of marriage as drive collapses",
        angle_pt="Esposa parou de convidar o marido pra treinar — falha silenciosa íntima do casamento conforme drive colapsa",
        hookCopy_en="\"Tom's wife had been leaving notes on the fridge for 6 months. He'd find one, mean to go, and at 7 PM he'd be on the couch. The notes stopped showing up. That's when he panicked.\"",
        hookCopy_pt="\"A esposa de Tom tinha deixado bilhetes na geladeira por 6 meses. Ele achava um, prometia ir, e às 7 da noite estava no sofá. Os bilhetes pararam de aparecer. Foi aí que ele entrou em pânico.\"",
        hookVisual_en="SHOCK CREATIVE (Phone photo): Refrigerator door — single yellow post-it handwritten by Jen: 'Tom — I made a cardio class reservation for us at 7. I'd love it if you came. Love, J.' Post-it dated 3 weeks ago (subtle date corner). Below it, 4 other older similar notes in a faded layered stack — all ignored. Single intimate element. [Category: Marital Disconnect]",
        hookVisual_pt="SHOCK CREATIVE (Foto celular): Porta da geladeira — único post-it amarelo escrito à mão por Jen: 'Tom — Reservei aula de cardio pra gente às 7. Adoraria se você fosse. Amor, J.' Post-it datado de 3 semanas atrás (canto sutil). Abaixo, 4 outros bilhetes similares antigos numa pilha desbotada — todos ignorados. Elemento único íntimo. [Category: Desconexão Conjugal]",
        format_en="Long-form native image (Format A — cold traffic narrative) | Skill: long-form-native-ad-writer",
        format_pt="Native long-form image (Format A — narrativa cold traffic) | Skill: long-form-native-ad-writer",
        speaker_en="Male first-person — Tom, 46, married 18 years to Jen",
        speaker_pt="Primeira pessoa masculina — Tom, 46, casado há 18 anos com Jen",
        execution_en="HEADLINE: 'My wife stopped inviting me to work out together. That's when I realized something was actually broken.' | NARRATIVE ~1800w (intimate/embarrassing per Derick): ESCALATION: Tom doesn't notice Jen has been silently quitting on him for months. He believed it was 'laziness' / 'busy season'. The day notes stop = panic moment. FAILED SOLUTIONS: motivation videos → cold showers → 'discipline' apps → therapy. MECHANISM: T-decline → dopamine reduction → behavioral anhedonia. Not character flaw, biochemistry. DISCOVERY: TMC. TRANSFORMATION: the day Tom writes the FIRST note to Jen. CTA (LEI #4).",
        execution_pt="HEADLINE: 'Minha esposa parou de me convidar pra treinar. Foi aí que entendi que algo estava realmente quebrado.' | NARRATIVA ~1800w (íntimo/constrangedor conforme Derick): ESCALATION: Tom não percebe que Jen tem desistido em silêncio dele há meses. Ele acreditava que era 'preguiça' / 'temporada cheia'. Dia que os bilhetes param = momento de pânico. FAILED SOLUTIONS: vídeos de motivação → banho gelado → apps de 'disciplina' → terapia. MECHANISM: T-decline → dopamina reduzida → anhedonia comportamental. Não é caráter, é bioquímica. DISCOVERY: TMC. TRANSFORMATION: o dia que Tom escreve o PRIMEIRO bilhete pra Jen. CTA (LEI #4).",
    ),

    # AD #29 — TMCAD-195 — Pixar: Dopamine character SHORT
    29: dict(
        angle_en="Personified dopamine narrates lost gym drive — brain chemistry visualized as Pixar character",
        angle_pt="Dopamina personificada narra perda de drive na academia — química cerebral visualizada como personagem Pixar",
        hookCopy_en="\"Hi, I'm your dopamine. And I haven't been able to get you to the gym in months.\"",
        hookCopy_pt="\"Oi, eu sou sua dopamina. E eu não consegui te levar pra academia há meses.\"",
        hookVisual_en="VISUAL HOOK (AI Animated 3D Pixar-Style): Dopamine character — small bright cute creature in a brain-control office — frantically tries to flip the 'GYM MOTIVATION' switch on the wall. Switch is broken. Cortisol villain holds the power cable, smirking from corner.",
        hookVisual_pt="VISUAL HOOK (Animação 3D AI Pixar-Style): Personagem dopamina — pequena criatura brilhante e fofa num escritório de controle do cérebro — tenta freneticamente acionar o switch 'MOTIVAÇÃO ACADEMIA' na parede. Switch está quebrado. Cortisol vilão segura o cabo de força, sorrindo de canto.",
        format_en="AI Animated Pixar-Style 3D | Validated internally",
        format_pt="Animação 3D AI Pixar-Style | Validado internamente",
        speaker_en="Dopamine personified (Pixar 3D character) — exhausted, sweet little creature trying to do her job against Cortisol's sabotage",
        speaker_pt="Dopamina personificada (personagem Pixar 3D) — pequena criatura doce e exausta tentando fazer seu trabalho contra a sabotagem do Cortisol",
        execution_en="DURATION 75s. Structure: \"Hi, I'm your [X]\". Dopamine explains what she does (drives motivation/reward) and why she can't anymore (cortisol blocking, T support gone). TMC reveal: ashwagandha cuts cortisol → dopamine signaling restored. Speaker IMPREVISÍVEL + congruente (drive = dopamine). Point-of-pain SPECIFIC (can't get to the gym in months). CTA with 'they'll'.",
        execution_pt="DURAÇÃO 75s. Estrutura: \"Oi, eu sou sua [X]\". Dopamina explica o que ela faz (gera motivação/reward) e por que não consegue mais (cortisol bloqueando, suporte T sumido). TMC revela: ashwagandha corta cortisol → sinalização dopamina restaurada. Speaker IMPREVISÍVEL + congruente. Point-of-pain ESPECÍFICO (não consegue ir na academia há meses). CTA com 'they'll'.",
    ),

    # AD #30 — TMCAD-196 — Pixar: Dopamine vs Cortisol war SHORT
    30: dict(
        angle_en="War in your brain — Dopamine (victim) vs Cortisol (villain) battle for gym motivation",
        angle_pt="Guerra no seu cérebro — Dopamina (vítima) vs Cortisol (vilão) lutando pela motivação na academia",
        hookCopy_en="\"There's a war happening in your brain every time you try to go to the gym. And right now, the wrong side is winning.\"",
        hookCopy_pt="\"Tem uma guerra rolando no seu cérebro toda vez que você tenta ir na academia. E agora, o lado errado tá ganhando.\"",
        hookVisual_en="VISUAL HOOK (AI Animated 3D Pixar-Style): Direct dialogue battle inside the brain. Cortisol (fat arrogant villain) shouts: \"STAY ON THE COUCH!\" Dopamine (small, hopeful) whispers: \"Please go...\" Visual = lopsided fight. Cortisol wins easily.",
        hookVisual_pt="VISUAL HOOK (Animação 3D AI Pixar-Style): Batalha de diálogo direto dentro do cérebro. Cortisol (vilão gordo arrogante) grita: \"FIQUE NO SOFÁ!\" Dopamina (pequena, esperançosa) sussurra: \"Por favor vai...\" Visual = luta desigual. Cortisol vence fácil.",
        format_en="AI Animated Pixar-Style 3D | Validated internally",
        format_pt="Animação 3D AI Pixar-Style | Validado internamente",
        speaker_en="Dopamine + Cortisol (Pixar 3D characters) in shared universe with AD#9, #10, #29",
        speaker_pt="Dopamina + Cortisol (personagens Pixar 3D) em universo compartilhado com AD#9, #10, #29",
        execution_en="DURATION 75s. \"War in your brain\" hook opens multiple loops + Pixar visualizes brilliantly. Mechanism: cortisol blocks dopamine reward circuits → motivation circuits literally rewired. TMC ingredients enter as reinforcements for dopamine's side. Cumulative storytelling continuity (shared universe). CTA with 'they'll'.",
        execution_pt="DURAÇÃO 75s. Hook \"guerra no seu cérebro\" abre múltiplos loops + Pixar visualiza brilhantemente. Mecanismo: cortisol bloqueia circuitos de reward de dopamina → circuitos de motivação literalmente recableados. Ingredientes TMC entram como reforços do lado da dopamina. Continuidade de storytelling cumulativa (universo compartilhado). CTA com 'they'll'.",
    ),

    # AD #31 — TMCAD-197 — Pixar: Dopamine flashbacks MID
    31: dict(
        angle_en="Dopamine narrates nostalgic flashbacks of glory days — emotional Pixar storytelling about lost gym love",
        angle_pt="Dopamina narra flashbacks nostálgicos dos tempos de glória — storytelling Pixar emocional sobre amor perdido pela academia",
        hookCopy_en="\"Hi, I'm your dopamine. Let me show you why you used to LOVE the gym — and what changed.\"",
        hookCopy_pt="\"Oi, eu sou sua dopamina. Deixa eu te mostrar por que você AMAVA a academia — e o que mudou.\"",
        hookVisual_en="VISUAL HOOK (AI Animated 3D Pixar-Style): Dopamine character opens an animated photo album. Pages flip — Pixar-style flashbacks of viewer at 28, energized at the gym, post-workout euphoria, social high-fives. Then album smokes/darkens at recent pages. Live transformation visualizes T-decline + cortisol takeover.",
        hookVisual_pt="VISUAL HOOK (Animação 3D AI Pixar-Style): Personagem Dopamina abre álbum de fotos animado. Páginas viram — flashbacks Pixar do espectador aos 28, energizado na academia, euforia pós-treino, high-fives sociais. Aí álbum fumega/escurece nas páginas recentes. Transformação ao vivo visualiza T-decline + tomada de poder do cortisol.",
        format_en="AI Animated Pixar-Style 3D — MID format with flashback storytelling (2:20)",
        format_pt="Animação 3D AI Pixar-Style — formato MID com storytelling de flashback (2:20)",
        speaker_en="Dopamine personified (Pixar 3D, continuity from AD#29-30)",
        speaker_pt="Dopamina personificada (Pixar 3D, continuity dos AD#29-30)",
        execution_en="DURATION 2:20. Maintains personification, expands to Pixar storytelling with flashbacks. Mechanism via emotion: dopamine wasn't always weak — she had support (T, low cortisol). TMC restores her support team. Speaker continuity creates serialized entertainment. CTA with 'they'll'.",
        execution_pt="DURAÇÃO 2:20. Mantém personificação, expande pra storytelling Pixar com flashbacks. Mecanismo via emoção: dopamina nem sempre foi fraca — ela tinha suporte (T, cortisol baixo). TMC restaura sua equipe de suporte. Continuidade de speaker cria entretenimento serializado. CTA com 'they'll'.",
    ),

    # AD #32 — TMCAD-198 — Pixar: Cortisol confessing crimes MID
    32: dict(
        angle_en="Cortisol villain confesses his crimes with sarcastic humor — entertainment-first DR via Pixar villain monologue",
        angle_pt="Cortisol vilão confessa suas crimes com humor sarcástico — DR entretenimento-first via monólogo vilão Pixar",
        hookCopy_en="\"Hi, I'm cortisol. And I've been wrecking your gym game for 5 years now. Let me show you how.\"",
        hookCopy_pt="\"Oi, eu sou seu cortisol. E venho destruindo sua academia há 5 anos agora. Deixa eu te mostrar como.\"",
        hookVisual_en="VISUAL HOOK (AI Animated 3D Pixar-Style): Cortisol villain seated in malicious armchair (Mr. Burns vibe), fingers steepled, smiling. Behind him, a giant evidence wall covered in Polaroids of viewer's failed gym attempts, missed sessions, lost workouts. \"I've been busy.\"",
        hookVisual_pt="VISUAL HOOK (Animação 3D AI Pixar-Style): Cortisol vilão sentado em poltrona maliciosa (vibe Mr. Burns), dedos cruzados, sorrindo. Atrás dele, uma parede gigante de evidências coberta de Polaroids das tentativas falhas de academia, sessões perdidas, treinos perdidos. \"Tô ocupado.\"",
        format_en="AI Animated Pixar-Style 3D — Pixar villain monologue (2:30)",
        format_pt="Animação 3D AI Pixar-Style — monólogo vilão Pixar (2:30)",
        speaker_en="Cortisol villain (Pixar 3D, continuity from AD#9, #10, #30)",
        speaker_pt="Cortisol vilão (Pixar 3D, continuity dos AD#9, #10, #30)",
        execution_en="DURATION 2:30. Pixar villain narrating his own crimes = pure entertainment with embedded education. Cortisol explains step-by-step how he sabotages: blocks T production, hijacks dopamine, fragments sleep, drains adrenals. TMC heroes (ashwagandha primary) arrive at end and put him in handcuffs. Imprevisível, congruente, multi-loop. CTA with 'they'll'.",
        execution_pt="DURAÇÃO 2:30. Vilão Pixar narrando suas próprias crimes = entretenimento puro com educação embutida. Cortisol explica passo a passo como ele sabota: bloqueia produção T, sequestra dopamina, fragmenta sono, drena adrenais. Heróis TMC (ashwagandha principal) chegam no final e o algemam. Imprevisível, congruente, multi-loop. CTA com 'they'll'.",
    ),

    # AD #33 — TMCAD-199 — Pixar: Defeated Testosterone MID
    33: dict(
        angle_en="Personified testosterone admits responsibility for lost gym drive — 'Not your fault — it's mine' character reframe",
        angle_pt="Testosterona personificada assume responsabilidade pelo drive perdido — reframe de personagem 'Não é sua culpa — é minha'",
        hookCopy_en="\"Hi, I'm your testosterone. And I haven't gotten you to the gym since 2023. It's not your fault — it's mine.\"",
        hookCopy_pt="\"Oi, eu sou sua testosterona. E eu não te levei pra academia desde 2023. Não é sua culpa — é minha.\"",
        hookVisual_en="VISUAL HOOK (AI Animated 3D Pixar-Style): T character — defeated, smaller version — sitting on a Pixar-style couch inside the body, holding a tiny beer. Dusty gym clothes piled in corner. Empty gym bag with cobwebs. T addresses viewer with apologetic expression.",
        hookVisual_pt="VISUAL HOOK (Animação 3D AI Pixar-Style): Personagem T — derrotada, versão menor — sentada num sofá estilo Pixar dentro do corpo, segurando uma cervejinha. Roupa de academia empoeirada num canto. Mochila vazia com teias de aranha. T se dirige ao espectador com expressão de desculpas.",
        format_en="AI Animated Pixar-Style 3D — testosterone character monologue (2:40)",
        format_pt="Animação 3D AI Pixar-Style — monólogo personagem testosterona (2:40)",
        speaker_en="Testosterone personified (Pixar 3D, continuity from AD#21, #22)",
        speaker_pt="Testosterona personificada (Pixar 3D, continuity dos AD#21, #22)",
        execution_en="DURATION 2:40. \"Not your fault\" reframe = exact 'Not Laziness' angle, but executed by personified T. Removes shame, opens emotional door. T explains the cascade in first-person: cortisol pressure, SHBG trap, dopamine breakdown. TMC = T's support team coming back. CTA with 'they'll'.",
        execution_pt="DURAÇÃO 2:40. Reframe \"Não é sua culpa\" = exato ângulo 'Não é Preguiça', mas executado pela T personificada. Remove vergonha, abre porta emocional. T explica a cascata em primeira pessoa: pressão do cortisol, armadilha SHBG, breakdown da dopamina. TMC = equipe de suporte da T voltando. CTA com 'they'll'.",
    ),

    # AD #34 — TMCAD-200 — Pixar LONG: Kingdom under siege Mini-VSL
    34: dict(
        angle_en="Mini-VSL Pixar epic — kingdom inside the body under siege, T as deposed mayor, ingredients as resistance heroes",
        angle_pt="Mini-VSL Pixar épico — reino dentro do corpo sob cerco, T como prefeito deposto, ingredientes como heróis da resistência",
        hookCopy_en="\"There's a city inside you that runs your gym game. It's been under siege since you turned 40. Let me tell you who's fighting for you.\"",
        hookCopy_pt="\"Tem uma cidade dentro de você que comanda sua academia. Ela está sob cerco desde que você fez 40. Deixa eu te contar quem tá lutando por você.\"",
        hookVisual_en="VISUAL HOOK (AI Animated 3D Pixar-Style): Aerial shot of an epic stylized city inside the body. T as deposed mayor, exiled. Cortisol governs from a black tower. SHBG locks T in a castle. Dopamine cries on a balcony. Resistance forms in shadows. Boron + L-Citrulline arrive as caped heroes through city gates.",
        hookVisual_pt="VISUAL HOOK (Animação 3D AI Pixar-Style): Plano aéreo de uma cidade épica estilizada dentro do corpo. T como prefeito deposto, exilado. Cortisol governa de uma torre negra. SHBG tranca T num castelo. Dopamina chora numa varanda. Resistência se forma nas sombras. Boron + L-Citrulina chegam como heróis com capas pelas portas da cidade.",
        format_en="AI Animated Pixar-Style 3D — Mini-VSL épico (3:30)",
        format_pt="Animação 3D AI Pixar-Style — Mini-VSL épico (3:30)",
        speaker_en="Cast Pixar 3D — T (fallen hero), Cortisol (villain), SHBG (jailer), Boron (liberator), L-Citrulline (messenger), Vein (executor) — narrator: omniscient",
        speaker_pt="Cast Pixar 3D — T (herói caído), Cortisol (vilão), SHBG (carcereiro), Boron (libertador), L-Citrulina (mensageiro), Veia (executora) — narrador: onisciente",
        execution_en="DURATION 3:30 (not 4:30 — Pixar works better <4min). Storytelling épico Pixar — entretenimento puro. Mechanism virou narrativa de guerra. Resistance forms, ingredients arrive as heroes one by one, retake the city. End: T crowned again. TMC presented as the alliance that brings them all together. CTA with 'they'll'. Cumpre voice-criteria 'ad inteiro nativamente curioso'.",
        execution_pt="DURAÇÃO 3:30 (não 4:30 — Pixar funciona melhor <4min). Storytelling épico Pixar — entretenimento puro. Mecanismo virou narrativa de guerra. Resistência se forma, ingredientes chegam como heróis um por um, retomam a cidade. Fim: T coroada de novo. TMC apresentado como a aliança que os une. CTA com 'they'll'. Cumpre voice-criteria 'ad inteiro nativamente curioso'.",
    ),

    # AD #35 — TMCRMKT-32 — RTG Video: $140 thrown away (cost-pain)
    35: dict(
        angle_en="Cost-pain reframe — viewer realizes monthly supplement spend is wasted without cortisol/T foundation",
        angle_pt="Reframe cost-pain — espectador percebe que gasto mensal em suplementos é desperdiçado sem foundation cortisol/T",
        hookCopy_en="\"Last month I threw away $140 of supplements. Then I bought one cup of coffee instead.\"",
        hookCopy_pt="\"Mês passado eu joguei $140 de suplementos no lixo. Aí comprei uma cup de café no lugar.\"",
        hookVisual_en="VISUAL HOOK (VO-over-B-roll, validated Mars Men 'Borrowing' format): Hand grabbing supplement bottles from kitchen shelf and dropping each one into a trash can. Dollar overlays appear: Lion's Mane $30, Tongkat Ali $40, Ashwagandha $50, Boron $20. Total: $140/month. Cut to TMC bag landing on counter triumphantly.",
        hookVisual_pt="VISUAL HOOK (VO-sobre-B-roll, formato validado Mars Men 'Borrowing'): Mão pegando potes de suplementos da prateleira da cozinha e jogando um por um no lixo. Overlays de dólar aparecem: Lion's Mane $30, Tongkat Ali $40, Ashwagandha $50, Boron $20. Total: $140/mês. Corte pra bag de TMC pousando triunfante na bancada.",
        format_en="VO-over-B-roll montage | RTG Video | Format validated Mars Men 'Borrowing'",
        format_pt="VO-sobre-B-roll montagem | RTG Video | Formato validado Mars Men 'Borrowing'",
        speaker_en="Male VO 40-50, energetic narrator (no on-camera speaker — cost-pain montage)",
        speaker_pt="VO masculino 40-50, narrador energético (sem speaker on-camera — montagem cost-pain)",
        execution_en="DURATION 60s (RTG). Per Derick feedback: new idea required. Cost-pain hook (Life Cykel pattern, hook-grade). Math reveal: TMC includes everything in those bottles at clinical doses + the foundation (ashwagandha) the others lack. Visual ação primeiro frame (V-4). CTA with 'we'll' (brand voice-over): 365-day money-back, 40% off + free shipping (LEI #4).",
        execution_pt="DURAÇÃO 60s (RTG). Conforme feedback do Derick: nova ideia requerida. Cost-pain hook (Life Cykel pattern, hook-grade). Revelação matemática: TMC inclui tudo daqueles potes em doses clínicas + a foundation (ashwagandha) que os outros não têm. Ação visual primeiro frame (V-4). CTA com 'we'll' (brand voice-over): 365-day money-back, 40% off + frete grátis (LEI #4).",
    ),

    # ──────────────────────────────────────────────────
    # QUINTA — C2 / NO PUMP
    # ──────────────────────────────────────────────────

    # AD #39 — TMCIMG-157 — Native rewrite: Old Instagram (intimate)
    39: dict(
        angle_en="Married man finds 2018 Instagram photo of his peak body — visual proof of decline as intimate shame trigger",
        angle_pt="Homem casado acha foto de Instagram de 2018 do seu corpo no auge — prova visual de decadência como gatilho íntimo de vergonha",
        hookCopy_en="\"Steve hadn't taken a shirtless photo in three years. He found one from 2018 on his old Instagram. The man in the photo looked like a stranger he used to be.\"",
        hookCopy_pt="\"Steve não tirava uma foto sem camisa há três anos. Encontrou uma de 2018 no Instagram antigo dele. O homem da foto parecia um estranho que ele costumava ser.\"",
        hookVisual_en="SHOCK CREATIVE (Phone screenshot side-by-side): LEFT: Old Instagram post from 2018 — Steve flexing on a beach, veins visible, completely 'swoll', caption '53 and crushing it!' 247 likes. RIGHT: Recent bathroom mirror selfie — same arm, completely flat, no veins, no definition, no pump. Single screenshot, two states. [Category: Identity Loss / Body Shame]",
        hookVisual_pt="SHOCK CREATIVE (Screenshot celular side-by-side): ESQUERDA: Post antigo do Instagram de 2018 — Steve flexionando na praia, veias visíveis, completamente 'swoll', caption '53 and crushing it!' 247 likes. DIREITA: Selfie recente no espelho do banheiro — mesmo braço, completamente plano, sem veias, sem definição, sem pump. Único screenshot, dois estados. [Category: Identity Loss / Body Shame]",
        format_en="Long-form native image (Format A — cold traffic narrative) | Skill: long-form-native-ad-writer",
        format_pt="Native long-form image (Format A — narrativa cold traffic) | Skill: long-form-native-ad-writer",
        speaker_en="Male first-person — Steve, 53, married 22 years",
        speaker_pt="Primeira pessoa masculina — Steve, 53, casado há 22 anos",
        execution_en="HEADLINE: 'I found a photo of myself from 2018 that I don't remember being able to take anymore.' | NARRATIVE ~1800w (intimate/embarrassing per Derick): ESCALATION: Steve hides old photos on iPhone, stops going to pool with kids, buys looser shirts. Day he randomly opens Instagram — SHOCK MOMENT. He takes off shirt, flexes, snaps photo. Contrast devastating. FAILED SOLUTIONS: expensive pre-workout → L-citrulline → arginine → doctor said 'you're 53'. MECHANISM: NO pathway depends on T + endothelial function. T dropped, NO production crashed. DISCOVERY: TMC. TRANSFORMATION: the photo he takes again, 4 months later. CTA (LEI #4).",
        execution_pt="HEADLINE: 'Encontrei uma foto minha de 2018 que não me lembro mais de conseguir tirar.' | NARRATIVA ~1800w (íntimo/constrangedor conforme Derick): ESCALATION: Steve esconde fotos antigas no iPhone, para de ir na piscina com filhos, compra camisas mais largas. Dia que abre Instagram aleatório — MOMENTO DE CHOQUE. Tira camisa, flexiona, tira foto. Contraste devastador. FAILED SOLUTIONS: pre-workout caro → L-citrulina → arginina → médico falou 'você tem 53'. MECHANISM: via NO depende de T + função endotelial. T caiu, produção de NO desabou. DISCOVERY: TMC. TRANSFORMATION: a foto que ele tira de novo, 4 meses depois. CTA (LEI #4).",
    ),

    # AD #40 — TMCIMG-158 — Native rewrite: Wife observes (intimate, LEI #10)
    40: dict(
        angle_en="Wife silently observes husband measuring his arm in secret — story 100% about him (LEI #10), narrated through her eyes",
        angle_pt="Esposa observa em silêncio marido medindo o braço em segredo — história 100% sobre ele (LEI #10), narrada pelos olhos dela",
        hookCopy_en="\"Lisa walked into their bedroom and froze. Mike was flexing in the closet mirror, measuring his bicep with a tape. The number was the same as the year before. She closed the door quietly and didn't tell him she'd seen.\"",
        hookCopy_pt="\"Lisa entrou no quarto deles e congelou. Mike estava flexionando no espelho do closet, medindo o bíceps com uma fita métrica. O número era o mesmo do ano anterior. Ela fechou a porta em silêncio e não disse que tinha visto.\"",
        hookVisual_en="SHOCK CREATIVE (Phone photo): Tape measure wrapped around Mike's flexed left bicep, reading '13.5 in.' Tape held tight (measuring flexed). Behind him, in the closet mirror reflection, Lisa is visible at the doorframe, watching silently — Mike doesn't see her. Single intimate moment. [Category: Marital Intimacy / Hidden Decline]",
        hookVisual_pt="SHOCK CREATIVE (Foto celular): Fita métrica em volta do bíceps esquerdo flexionado de Mike, marcando '13.5 in'. Fita apertada (medindo flexionado). Atrás dele, no reflexo do espelho do closet, Lisa é visível no batente da porta, observando em silêncio — Mike não a vê. Momento único íntimo. [Category: Intimidade Conjugal / Decadência Escondida]",
        format_en="Long-form native image (Format A — cold traffic narrative) | Skill: long-form-native-ad-writer",
        format_pt="Native long-form image (Format A — narrativa cold traffic) | Skill: long-form-native-ad-writer",
        speaker_en="Wife POV (Lisa narrator) — story 100% about him (Mike, 54), married 26 years. LEI #10 compliant.",
        speaker_pt="POV esposa (Lisa narradora) — história 100% sobre ele (Mike, 54), casados há 26 anos. LEI #10 cumprida.",
        execution_en="HEADLINE: 'I caught my husband measuring his arm in our bedroom. He didn't see me. I didn't say anything for a week.' | NARRATIVE ~1800w (intimate/embarrassing per Derick, LEI #10): NARRATOR Lisa, 100% about Mike. ESCALATION: Lisa observes Mike hiding his body — stops taking shirt off at home, secret notebook with measurements, buys tape measure. She knows him. He has to find it himself. FAILED SOLUTIONS through Mike (Lisa watches): TRT consultation declined → SHBG mention without explanation. MECHANISM (Lisa researches in secret): SHBG trapping. T present but inactive. DISCOVERY (she leaves a folder about TMC 'casually' on counter). TRANSFORMATION: Mike taking his shirt off at home again. CTA (LEI #4).",
        execution_pt="HEADLINE: 'Peguei meu marido medindo o braço no nosso quarto. Ele não me viu. Eu não disse nada por uma semana.' | NARRATIVA ~1800w (íntimo/constrangedor conforme Derick, LEI #10): NARRADORA Lisa, 100% sobre Mike. ESCALATION: Lisa observa Mike escondendo o corpo — para de tirar camisa em casa, caderno secreto com medidas, compra fita métrica. Ela conhece ele. Ele tem que descobrir sozinho. FAILED SOLUTIONS via Mike (Lisa observa): consulta TRT declinada → menção a SHBG sem explicação. MECHANISM (Lisa pesquisa em segredo): aprisionamento SHBG. T presente mas inativo. DISCOVERY (ela deixa pasta sobre TMC 'casualmente' na bancada). TRANSFORMATION: Mike tirando camisa em casa de novo. CTA (LEI #4).",
    ),

    # AD #41 — TMCAD-203 — Pixar: Vein character SHORT
    41: dict(
        angle_en="Personified vein apologizes for failing to give pumps — blood flow visualized as exhausted Pixar character",
        angle_pt="Veia personificada se desculpa por falhar em dar pumps — fluxo sanguíneo visualizado como personagem Pixar exausta",
        hookCopy_en="\"Hi, I'm your vein. And I haven't been able to give you a real pump in 3 years.\"",
        hookCopy_pt="\"Oi, eu sou sua veia. E eu não consegui te dar um pump de verdade nos últimos 3 anos.\"",
        hookVisual_en="VISUAL HOOK (AI Animated 3D Pixar-Style): Animated vein character — skinny, frustrated, smaller than she should be. Tries to inflate her tube but only coughs out a weak puff of air. Looks at the muscle next to her sadly: \"Sorry, buddy.\" Muscle character (defeated) gives a thumbs-down.",
        hookVisual_pt="VISUAL HOOK (Animação 3D AI Pixar-Style): Personagem veia animada — magrinha, frustrada, menor do que deveria ser. Tenta inflar o tubo dela mas só tosse um vento fraco. Olha pro músculo ao lado dela tristemente: \"Foi mal, parceiro.\" Personagem músculo (derrotado) dá um polegar pra baixo.",
        format_en="AI Animated Pixar-Style 3D | Validated internally",
        format_pt="Animação 3D AI Pixar-Style | Validado internamente",
        speaker_en="Vein personified (Pixar 3D character) — exhausted, apologetic vascular character",
        speaker_pt="Veia personificada (personagem Pixar 3D) — personagem vascular exausta, pedindo desculpas",
        execution_en="DURATION 70s. Structure: \"Hi, I'm your [X]\" validated. Vein explains NO pathway: she needs nitric oxide to vasodilate, NO needs L-citrulline + endothelial function. T-decline killed her engine. TMC = L-citrulline + tongkat ali (T support). Speaker IMPREVISÍVEL + congruente (no pump = blood flow). Point-of-pain instantâneo. CTA with 'they'll'.",
        execution_pt="DURAÇÃO 70s. Estrutura: \"Oi, eu sou sua [X]\" validada. Veia explica via NO: ela precisa de óxido nítrico pra vasodilatar, NO precisa de L-citrulina + função endotelial. T-decline matou o motor dela. TMC = L-citrulina + tongkat ali (suporte T). Speaker IMPREVISÍVEL + congruente. Point-of-pain instantâneo. CTA com 'they'll'.",
    ),

    # AD #42 — TMCAD-204 — Hook A approved + Pixar SHBG cárcere
    42: dict(
        angle_en="Approved Hook A executed in Pixar — SHBG as literal jailer, 98% of T trapped behind bars",
        angle_pt="Hook A aprovado executado em Pixar — SHBG como carcereiro literal, 98% de T preso atrás de barras",
        hookCopy_en="\"98% of your testosterone is trapped. And that's why your workouts aren't working.\"",
        hookCopy_pt="\"98% da sua testosterona está presa. E é por isso que seus treinos não estão funcionando.\"",
        hookVisual_en="VISUAL HOOK (AI Animated 3D Pixar-Style): Testosterone (Pixar character) trapped behind iron bars in a SHBG-shaped molecular prison. SHBG personified as fat smug guard with keys jangling. Camera dolly out reveals 98 other T's also trapped, only 2 free outside the cage. T shakes the bars, frustrated: \"98% of me is locked in here.\"",
        hookVisual_pt="VISUAL HOOK (Animação 3D AI Pixar-Style): Testosterona (personagem Pixar) presa atrás de barras de ferro numa prisão molecular em formato SHBG. SHBG personificado como guarda gordo prepotente com chaves balançando. Câmera dolly out revela outros 98 Ts também presos, só 2 livres lá fora. T balança as barras, frustrada: \"98% de mim está preso aqui.\"",
        format_en="AI Animated Pixar-Style 3D | Validated internally — Hook A approved by Derick",
        format_pt="Animação 3D AI Pixar-Style | Validado internamente — Hook A aprovado pelo Derick",
        speaker_en="Testosterone trapped (Pixar 3D, continuity from AD#21, #22, #33) + SHBG jailer character",
        speaker_pt="Testosterona presa (Pixar 3D, continuity dos AD#21, #22, #33) + personagem carcereiro SHBG",
        execution_en="DURATION 75s. Hook approved by Derick + Pixar elite execution. SHBG as literal prison villain = maximum congruence. Boron arrives as hero with the key, releases the trapped T. Speaker IMPREVISÍVEL + congruente. Point-of-pain SPECIFIC (98% trapped). CTA with 'they'll'.",
        execution_pt="DURAÇÃO 75s. Hook aprovado pelo Derick + execução Pixar elite. SHBG como vilão de prisão literal = congruência máxima. Boron chega como herói com a chave, liberta as Ts presas. Speaker IMPREVISÍVEL + congruente. Point-of-pain ESPECÍFICO (98% preso). CTA com 'they'll'.",
    ),

    # AD #43 — TMCAD-205 — Pixar: Vein + Muscle buddy-cop MID
    43: dict(
        angle_en="Buddy-cop dynamic — Vein and Muscle (Pixar 3D) blame each other for missing pumps",
        angle_pt="Dinâmica buddy-cop — Veia e Músculo (Pixar 3D) culpam um ao outro pela falta de pumps",
        hookCopy_en="\"Hi, I'm your vein. This is your muscle. And we haven't been working together since you turned 50.\"",
        hookCopy_pt="\"Oi, eu sou sua veia. Esse é seu músculo. E a gente não trabalha junto desde que você fez 50.\"",
        hookVisual_en="VISUAL HOOK (AI Animated 3D Pixar-Style): Vein character (skinny, anxious) tries to pump blood. Muscle character (defeated, slumped) waits anxiously. Muscle: \"Bro, where's my pump?\" Vein: \"I'M TRYING, MAN.\" Comedic frustrated dialogue, both fail, both blame each other.",
        hookVisual_pt="VISUAL HOOK (Animação 3D AI Pixar-Style): Personagem Veia (magrinha, ansiosa) tenta bombear sangue. Personagem Músculo (derrotado, encurvado) espera ansioso. Músculo: \"Bro, cadê meu pump?\" Veia: \"TÔ TENTANDO, CARA.\" Diálogo cômico frustrado, os dois falham, os dois se culpam.",
        format_en="AI Animated Pixar-Style 3D — buddy-cop dynamic (2:20)",
        format_pt="Animação 3D AI Pixar-Style — dinâmica buddy-cop (2:20)",
        speaker_en="Vein + Muscle (Pixar 3D characters, continuity from AD#18, #41)",
        speaker_pt="Veia + Músculo (personagens Pixar 3D, continuity dos AD#18, #41)",
        execution_en="DURATION 2:20. Buddy-cop dynamic Pixar = pure entertainment. Multiple loops (que dupla maluca? por que não trabalham?). Mechanism explained via dialogue: vein needs L-citrulline (NO), muscle needs T support, both need cortisol gone. TMC = team manager that fixes them both. Cumulative entertainment storytelling. CTA with 'they'll'.",
        execution_pt="DURAÇÃO 2:20. Dinâmica buddy-cop Pixar = entretenimento puro. Múltiplos loops (que dupla maluca? por que não trabalham?). Mecanismo explicado via diálogo: veia precisa de L-citrulina (NO), músculo precisa de suporte T, ambos precisam que cortisol vá embora. TMC = gerente do time que conserta os dois. Entretenimento storytelling cumulativo. CTA com 'they'll'.",
    ),

    # AD #44 — TMCAD-206 — Pixar: Boron rescue MID
    44: dict(
        angle_en="Boron arrives as caped Pixar hero to break T out of SHBG prison — rescue narrative as mechanism reveal",
        angle_pt="Boron chega como herói Pixar com capa pra quebrar T da prisão SHBG — narrativa de resgate como revelação de mecanismo",
        hookCopy_en="\"Most of your testosterone is locked in a cage. There's one mineral that can break the lock — and you're probably not getting enough of it.\"",
        hookCopy_pt="\"A maior parte da sua testosterona está trancada numa jaula. Existe um mineral que pode quebrar a fechadura — e você provavelmente não está tomando o suficiente.\"",
        hookVisual_en="VISUAL HOOK (AI Animated 3D Pixar-Style): SHBG molecular prison cell. T (defeated, multiple copies) trapped behind bars. Boron (caped Pixar hero with B insignia) walks in dramatic slow-motion, plants himself in front of cell: \"I'm here to break you out.\" Lock cracks. Cinematic Pixar action.",
        hookVisual_pt="VISUAL HOOK (Animação 3D AI Pixar-Style): Cela de prisão molecular SHBG. T (derrotada, múltiplas cópias) presa atrás de barras. Boron (herói Pixar com capa e insígnia B) entra em câmera lenta dramática, se planta na frente da cela: \"Tô aqui pra te tirar.\" Fechadura racha. Ação cinematográfica Pixar.",
        format_en="AI Animated Pixar-Style 3D — rescue narrative (2:30)",
        format_pt="Animação 3D AI Pixar-Style — narrativa de resgate (2:30)",
        speaker_en="Boron (caped Pixar hero) + Testosterone (rescued character) + SHBG (defeated jailer) — continuity from AD#42",
        speaker_pt="Boron (herói Pixar com capa) + Testosterona (personagem resgatada) + SHBG (carcereiro derrotado) — continuity do AD#42",
        execution_en="DURATION 2:30. Storytelling de resgate Pixar = curiosidade total. Mechanism (SHBG/Boron) embedded in visual narrative. T explains: 'I was trapped for years. Then Boron showed up.' TMC contains 10mg Boron + tongkat ali + ashwagandha — the full liberation team. CTA with 'they'll'.",
        execution_pt="DURAÇÃO 2:30. Storytelling de resgate Pixar = curiosidade total. Mecanismo (SHBG/Boron) embutido em narrativa visual. T explica: 'Fiquei presa por anos. Aí Boron apareceu.' TMC contém 10mg de Boron + tongkat ali + ashwagandha — a equipe completa de libertação. CTA com 'they'll'.",
    ),

    # AD #46 — TMCAD-208 — Pixar LONG: Body city full ensemble Mini-VSL
    46: dict(
        angle_en="Mini-VSL Pixar épico — full ensemble cast in body city, mechanism virou narrativa de guerra (3:30)",
        angle_pt="Mini-VSL Pixar épico — elenco completo na cidade do corpo, mecanismo virou narrativa de guerra (3:30)",
        hookCopy_en="\"There's a city inside you that runs your gym game. It's been under siege since you turned 40. Let me tell you who's fighting for you.\"",
        hookCopy_pt="\"Tem uma cidade dentro de você que comanda sua academia. Ela está sob cerco desde que você fez 40. Deixa eu te contar quem tá lutando por você.\"",
        hookVisual_en="VISUAL HOOK (AI Animated 3D Pixar-Style): Aerial sweep of an epic stylized city inside the body. Empty gymnasium. Cracked roads. T as deposed mayor. Cortisol governing from black tower. SHBG castle. Vein pumping weakly. Resistance forms — Boron + L-Citrulline + Ashwagandha + Lion's Mane arrive as caped heroes through gates.",
        hookVisual_pt="VISUAL HOOK (Animação 3D AI Pixar-Style): Plano aéreo de uma cidade épica estilizada dentro do corpo. Ginásio vazio. Estradas rachadas. T como prefeito deposto. Cortisol governando da torre negra. Castelo SHBG. Veia bombeando fraco. Resistência se forma — Boron + L-Citrulina + Ashwagandha + Lion's Mane chegam como heróis com capa pelas portas.",
        format_en="AI Animated Pixar-Style 3D — Mini-VSL épico full ensemble (3:30)",
        format_pt="Animação 3D AI Pixar-Style — Mini-VSL épico elenco completo (3:30)",
        speaker_en="Cast Pixar 3D — T (fallen hero), Cortisol (villain), SHBG (jailer), Vein (executor), Boron (liberator), L-Citrulline (messenger), Ashwagandha (general advisor), Lion's Mane (mind keeper)",
        speaker_pt="Cast Pixar 3D — T (herói caído), Cortisol (vilão), SHBG (carcereiro), Veia (executora), Boron (libertador), L-Citrulina (mensageira), Ashwagandha (conselheira geral), Lion's Mane (guardiã da mente)",
        execution_en="DURATION 3:30. Mini-VSL Pixar épico — entretenimento puro. Cumpre voice-criteria 'ad nativamente curioso' ao extremo. Mechanism (T-decline + SHBG + cortisol + NO pathway) becomes ensemble war narrative. Ingredients arrive one by one as heroes. End: T crowned again, gym restored, city rebuilt. TMC = the alliance that brings them all. CTA with 'they'll'.",
        execution_pt="DURAÇÃO 3:30. Mini-VSL Pixar épico — entretenimento puro. Cumpre voice-criteria 'ad nativamente curioso' ao extremo. Mecanismo (T-decline + SHBG + cortisol + via NO) vira narrativa de guerra com elenco completo. Ingredientes chegam um por um como heróis. Fim: T coroada de novo, academia restaurada, cidade reconstruída. TMC = a aliança que une todos. CTA com 'they'll'.",
    ),

    # ──────────────────────────────────────────────────
    # SEXTA — C3 / BRAIN FOG
    # ──────────────────────────────────────────────────

    # AD #51 — TMCIMG-159 — Native rewrite: Son's school essay (intimate)
    51: dict(
        angle_en="12-year-old son writes school essay about dad's memory loss — teacher circles paragraph, dad finds it (intimate, embarrassing, paternal)",
        angle_pt="Filho de 12 anos escreve redação escolar sobre perda de memória do pai — professora circula parágrafo, pai encontra (íntimo, constrangedor, paternal)",
        hookCopy_en="\"Dan picked Tommy up from school and noticed the notebook on the kitchen table. He flipped through. He froze when he saw the circled paragraph. Tommy walked in, saw what Dan was reading, and quietly said: 'I didn't mean it bad, Dad.'\"",
        hookCopy_pt="\"Dan pegou Tommy na escola e notou o caderno na mesa da cozinha. Folheou. Congelou quando viu o parágrafo circulado. Tommy entrou, viu o que Dan estava lendo, e disse baixinho: 'Eu não quis dizer mal, Pai.'\"",
        hookVisual_en="SHOCK CREATIVE (Phone photo): 12-year-old's school notebook open to a handwritten essay titled 'My dad'. One paragraph circled in red pen by the teacher: 'My dad used to know everything. Now he forgets stuff a lot. I have to remind him about my baseball games sometimes.' Single page, intimate. Slightly out of focus background = kitchen table, family kitchen. [Category: Father-Son Disconnect / Generational Shame]",
        hookVisual_pt="SHOCK CREATIVE (Foto celular): Caderno escolar de criança de 12 anos aberto numa redação à mão intitulada 'Meu pai'. Um parágrafo circulado a caneta vermelha pela professora: 'Meu pai costumava saber tudo. Agora ele esquece muita coisa. Eu tenho que lembrá-lo dos meus jogos de baseball às vezes.' Página única, íntima. Fundo levemente fora de foco = mesa de cozinha, cozinha familiar. [Category: Desconexão Pai-Filho / Vergonha Geracional]",
        format_en="Long-form native image (Format A — cold traffic narrative) | Skill: long-form-native-ad-writer",
        format_pt="Native long-form image (Format A — narrativa cold traffic) | Skill: long-form-native-ad-writer",
        speaker_en="Male first-person — Dan, 49, father of Tommy (12)",
        speaker_pt="Primeira pessoa masculina — Dan, 49, pai de Tommy (12)",
        execution_en="HEADLINE: 'My 12-year-old wrote about me for a school assignment. The teacher circled one paragraph. I haven't been the same since.' | NARRATIVE ~1800w (intimate/embarrassing per Derick): ESCALATION through Dan: forgets son's baseball game (3 times), Tommy starts reminding Dan of things — generational role inversion. Dan thinks it's just stress. Day he finds the essay = devastating. FAILED SOLUTIONS: 8h sleep → cut coffee → meditation → neurologist ('nothing structural'). MECHANISM: chronic cortisol → BDNF suppressed → hippocampus literally shrinks. Ashwagandha cuts cortisol → BDNF recovers. Lion's Mane → NGF synthesis → neuroplasticity. DISCOVERY: TMC. TRANSFORMATION: Dan remembers the baseball game without reminders. CTA (LEI #4).",
        execution_pt="HEADLINE: 'Meu filho de 12 anos escreveu sobre mim numa tarefa escolar. A professora circulou um parágrafo. Não fui o mesmo desde então.' | NARRATIVA ~1800w (íntimo/constrangedor conforme Derick): ESCALATION via Dan: esquece o jogo de baseball do filho (3 vezes), Tommy começa a lembrar Dan das coisas — inversão geracional de papéis. Dan acha que é só estresse. Dia que encontra a redação = devastador. FAILED SOLUTIONS: dormir 8h → cortar café → meditação → neurologista ('nada estrutural'). MECHANISM: cortisol crônico → BDNF suprimido → hipocampo encolhe literalmente. Ashwagandha corta cortisol → BDNF se recupera. Lion's Mane → síntese NGF → neuroplasticidade. DISCOVERY: TMC. TRANSFORMATION: Dan lembra do jogo de baseball sem lembrete. CTA (LEI #4).",
    ),

    # AD #52 — TMCIMG-160 — Native rewrite: 9 post-its from wife (intimate)
    52: dict(
        angle_en="Wife silently writes notes for husband's appointments — he discovers 9 of them taped around the house (intimate, embarrassing, marital role inversion)",
        angle_pt="Esposa escreve em silêncio bilhetes pros compromissos do marido — ele descobre 9 deles colados pela casa (íntimo, constrangedor, inversão conjugal de papéis)",
        hookCopy_en="\"Chuck found a note on the bathroom mirror reminding him about the doctor's appointment he'd already missed twice. Then he started looking around. There were 9 notes. He counted them. He sat down on the toilet seat and didn't say anything for ten minutes.\"",
        hookCopy_pt="\"Chuck encontrou um bilhete no espelho do banheiro lembrando da consulta médica que ele já tinha perdido duas vezes. Aí começou a olhar em volta. Tinha 9 bilhetes. Ele contou. Sentou no vaso e não disse nada por dez minutos.\"",
        hookVisual_en="SHOCK CREATIVE (Phone photo): Yellow post-it taped to bathroom mirror, handwritten in blue marker by Karen (wife): 'TUESDAY: Dr. Patel 10am. Don't forget. Already missed twice.' Slight reflection of Chuck's bare shoulder visible in mirror corner. Single intimate domestic moment. [Category: Marital Role Reversal / Quiet Decline]",
        hookVisual_pt="SHOCK CREATIVE (Foto celular): Post-it amarelo colado no espelho do banheiro, escrito à mão com hidrocor azul por Karen (esposa): 'TERÇA: Dr. Patel 10h. Não esqueça. Já perdeu duas vezes.' Leve reflexo do ombro nu de Chuck visível no canto do espelho. Único momento íntimo doméstico. [Category: Inversão de Papéis Conjugal / Decadência Silenciosa]",
        format_en="Long-form native image (Format A — cold traffic narrative) | Skill: long-form-native-ad-writer",
        format_pt="Native long-form image (Format A — narrativa cold traffic) | Skill: long-form-native-ad-writer",
        speaker_en="Male first-person — Chuck, 52, owns small landscaping business, married",
        speaker_pt="Primeira pessoa masculina — Chuck, 52, dono de pequena empresa de jardinagem, casado",
        execution_en="HEADLINE: 'My wife has been writing me notes since I started forgetting my own appointments. Today I found 9 of them taped around the house.' | NARRATIVE ~1800w (intimate/embarrassing per Derick): ESCALATION: Chuck realizes Karen has silently been writing notes for weeks — she stopped asking, started just reminding. Chuck should be leading their life, now she's leading him. Embarrassment of being cared for like a child. FAILED SOLUTIONS: notebook → app → Adderall (off-label) → 'just stressed'. MECHANISM: cortisol → PFC impairment → executive function fails. DISCOVERY: TMC. TRANSFORMATION: the day Chuck writes the FIRST note to Karen ('Honey, dinner at Mario's at 7. I made the reservation.'). CTA (LEI #4).",
        execution_pt="HEADLINE: 'Minha esposa tem escrito bilhetes pra mim desde que comecei a esquecer minhas próprias consultas. Hoje encontrei 9 deles colados pela casa.' | NARRATIVA ~1800w (íntimo/constrangedor conforme Derick): ESCALATION: Chuck percebe que Karen vem escrevendo bilhetes em silêncio há semanas — ela parou de perguntar, passou a só lembrar. Chuck deveria estar liderando a vida deles, agora ela está liderando ele. Constrangimento de ser cuidado como criança. FAILED SOLUTIONS: caderno → app → Adderall (off-label) → 'só estressado'. MECHANISM: cortisol → impairment do PFC → função executiva falha. DISCOVERY: TMC. TRANSFORMATION: o dia que Chuck escreve o PRIMEIRO bilhete pra Karen ('Amor, jantar no Mario's às 7. Já reservei.'). CTA (LEI #4).",
    ),

    # AD #53 — TMCAD-211 — Hook B + Inside View (3 ashwagandha pots) — ZERO Google Trends
    53: dict(
        angle_en="Inside View visual hook — speaker physically demonstrates dose discrepancy across 3 ashwagandha brands (NO Google Trends, per Derick feedback)",
        angle_pt="Inside View visual hook — speaker fisicamente demonstra discrepância de dose entre 3 marcas de ashwagandha (SEM Google Trends, conforme feedback do Derick)",
        hookCopy_en="\"You're probably already taking ashwagandha. But you're probably taking it wrong.\"",
        hookCopy_pt="\"Você provavelmente já tá tomando ashwagandha. Mas provavelmente tá tomando errado.\"",
        hookVisual_en="VISUAL HOOK (Inside View — Derick favorite, voice-criteria V-2): Speaker in his kitchen grabs 3 different ashwagandha bottles (3 brands, different labels). Pours all 3 powders into a clear glass — each has different color/texture (KSM-66 vs root powder vs full-spectrum extract). Stirs to show discrepancy. Then dumps out 3/4 and shows 'this is the actual studied dose'. ZERO Google Trends imagery anywhere.",
        hookVisual_pt="VISUAL HOOK (Inside View — favorito Derick, voice-criteria V-2): Speaker na cozinha dele pega 3 potes diferentes de ashwagandha (3 marcas, rótulos diferentes). Despeja os 3 pós num copo transparente — cada um tem cor/textura diferente (KSM-66 vs root powder vs extrato full-spectrum). Mexe pra mostrar discrepância. Aí joga 3/4 fora e mostra 'esta é a dose realmente estudada'. ZERO imagery de Google Trends em nenhum momento.",
        format_en="UGC Talking Head (VH-001) with Inside View visual hook | Speaker: Male 48-55, supplement-savvy, kitchen",
        format_pt="UGC Talking Head (VH-001) com Inside View visual hook | Speaker: Masculino 48-55, supplement-savvy, cozinha",
        speaker_en="Male 48-55, supplement-savvy, in his home kitchen, casual but informed",
        speaker_pt="Masculino 48-55, supplement-savvy, na cozinha de casa, casual mas informado",
        execution_en="DURATION 75s. Hook B kept (Derick approved). Visual = Inside View (V-2 #5, validated). Speaker shows 3 pots: KSM-66 (real form, expensive) vs root powder (cheap, ineffective) vs full-spectrum (variable). Explains: most labels just say 'ashwagandha root' — that's not the studied form. TMC has KSM-66 at clinical dose. PubMed studies cited (NOT Google Trends per Derick feedback — it's data source for us, not argument for user). CTA with 'they'll'.",
        execution_pt="DURAÇÃO 75s. Hook B mantido (Derick aprovou). Visual = Inside View (V-2 #5, validado). Speaker mostra 3 potes: KSM-66 (forma real, cara) vs root powder (barato, ineficaz) vs full-spectrum (variável). Explica: a maioria dos rótulos só diz 'ashwagandha root' — isso não é a forma estudada. TMC tem KSM-66 na dose clínica. Estudos PubMed citados (NÃO Google Trends conforme feedback Derick — é fonte de dado pra gente, não argumento pro usuário). CTA com 'they'll'.",
    ),

    # AD #54 — TMCAD-212 — Hook A approved + Brain Pixar character
    54: dict(
        angle_en="Approved Hook A executed in Pixar — cute confused brain character literally lost in scenarios from each enumeration item",
        angle_pt="Hook A aprovado executado em Pixar — personagem cérebro fofo confuso literalmente perdido nos cenários de cada item da enumeração",
        hookCopy_en="\"You forgot where you parked. You reread the same email 3 times. You walked into a room and forgot why. Sound familiar?\"",
        hookCopy_pt="\"Você esqueceu onde estacionou. Releu o mesmo e-mail 3 vezes. Entrou num quarto e esqueceu por quê. Conhece?\"",
        hookVisual_en="VISUAL HOOK (AI Animated 3D Pixar-Style): Brain personified (Pixar 3D) — tired, dark circles, holding a confused yellow post-it. Cycle through 3 scenes matching enumeration: brain lost in giant parking lot holding 'Where's my car?' sign / brain rereading same email on giant laptop / brain walking through doorway then freezing mid-step. 'Detective Confused' little hat.",
        hookVisual_pt="VISUAL HOOK (Animação 3D AI Pixar-Style): Cérebro personificado (Pixar 3D) — cansado, com olheiras, segurando um post-it amarelo confuso. Ciclo por 3 cenas combinando com a enumeração: cérebro perdido num estacionamento gigante segurando placa 'Cadê meu carro?' / cérebro relendo o mesmo e-mail num laptop gigante / cérebro atravessando porta e congelando no meio do passo. Chapeuzinho 'Detetive Confuso'.",
        format_en="AI Animated Pixar-Style 3D | Validated internally — Hook A approved by Derick (Auri 9/10 enumeration pattern)",
        format_pt="Animação 3D AI Pixar-Style | Validado internamente — Hook A aprovado pelo Derick (padrão enumeração Auri 9/10)",
        speaker_en="Brain personified (Pixar 3D character) — exhausted, sweet, confused",
        speaker_pt="Cérebro personificado (personagem Pixar 3D) — exausto, fofo, confuso",
        execution_en="DURATION 80s. Hook validated (Auri 9/10 enumeration) + Pixar visualizing each enumeration item = elite. Speaker congruente (brain = brain fog), imprevisível (Pixar 3D), efeito WTF. Brain explains: cortisol → BDNF suppression → executive function fails. TMC = ashwagandha (cortisol cut) + Lion's Mane (NGF). Brain visibly recovers in transformation. CTA with 'they'll'.",
        execution_pt="DURAÇÃO 80s. Hook validado (enumeração Auri 9/10) + Pixar visualizando cada item da enumeração = elite. Speaker congruente (cérebro = brain fog), imprevisível (Pixar 3D), efeito WTF. Cérebro explica: cortisol → supressão BDNF → função executiva falha. TMC = ashwagandha (corte cortisol) + Lion's Mane (NGF). Cérebro visivelmente se recupera na transformação. CTA com 'they'll'.",
    ),

    # AD #55 — TMCAD-213 — Hook C + Disgusting POV (hippocampus shrinking) — ZERO Google Trends
    55: dict(
        angle_en="Hook C expanded — speaker reacts to disgusting medical timelapse of shrinking hippocampus (NO Google Trends, voice-criteria visual hook)",
        angle_pt="Hook C expandido — speaker reage a timelapse médico nojento de hipocampo encolhendo (SEM Google Trends, visual hook voice-criteria)",
        hookCopy_en="\"Can ashwagandha actually fix brain fog? I spent 40 hours reading the research. What I found nobody is talking about.\"",
        hookCopy_pt="\"Ashwagandha realmente conserta brain fog? Passei 40 horas lendo a pesquisa. O que encontrei ninguém tá falando.\"",
        hookVisual_en="VISUAL HOOK (Disgusting POV — Derick favorite, V-2 #6): Speaker reacts to a disgusting medical timelapse video on his laptop — shrinking hippocampus (real medical imaging, NOT CGI per voice-criteria V-5). Pauses, turns to camera with 'WTF I just learned this' expression. Bookshelves visible behind him in home library setup. ZERO Google Trends imagery anywhere.",
        hookVisual_pt="VISUAL HOOK (Disgusting POV — favorito Derick, V-2 #6): Speaker reage a um vídeo médico timelapse nojento no laptop dele — hipocampo encolhendo (imagem médica real, NÃO CGI conforme voice-criteria V-5). Pausa, vira pra câmera com expressão 'WTF acabei de aprender isso'. Estantes visíveis atrás dele em setup de biblioteca caseira. ZERO imagery de Google Trends.",
        format_en="UGC Talking Head + Disgusting POV insert | Speaker: Male 48-55, glasses, casual, home library | MID 2:20",
        format_pt="UGC Talking Head + insert Disgusting POV | Speaker: Masculino 48-55, óculos, casual, biblioteca caseira | MID 2:20",
        speaker_en="Male 48-55, wearing glasses, casual, in home library (bookshelves behind)",
        speaker_pt="Masculino 48-55, de óculos, casual, em biblioteca caseira (estantes atrás)",
        execution_en="DURATION 2:20. Hook C kept (Derick approved + expand). Visual = Disgusting POV (V-2 #6, Derick favorite). Speaker tells personal research journey. Cites PubMed studies (NOT Google Trends per Derick — Google Trends é fonte interna, não argumento). Mechanism: cortisol → BDNF suppression → hippocampus shrinks (LEI #7: Lion's Mane apoia BDNF, never 'deficiency'). Lion's Mane → BDNF/NGF → neurogenesis. TMC has both. CTA with 'they'll'.",
        execution_pt="DURAÇÃO 2:20. Hook C mantido (Derick aprovou + expandir). Visual = Disgusting POV (V-2 #6, favorito Derick). Speaker conta jornada pessoal de pesquisa. Cita estudos PubMed (NÃO Google Trends conforme Derick — Google Trends é fonte interna, não argumento). Mecanismo: cortisol → supressão BDNF → hipocampo encolhe (LEI #7: Lion's Mane apoia BDNF, nunca 'deficiência'). Lion's Mane → BDNF/NGF → neurogênese. TMC tem ambos. CTA com 'they'll'.",
    ),

    # AD #56 — TMCAD-214 — New Pixar concept: BDNF character
    56: dict(
        angle_en="Personified BDNF (the brain's fertilizer) is being killed by cortisol — completely new Pixar concept per Derick rewrite request",
        angle_pt="BDNF personificada (o fertilizante do cérebro) está sendo morta pelo cortisol — conceito Pixar completamente novo conforme pedido de rewrite do Derick",
        hookCopy_en="\"Hi, I'm BDNF. I'm the reason your brain remembers things. And cortisol has been killing me for 5 years.\"",
        hookCopy_pt="\"Oi, eu sou BDNF. Sou o motivo do seu cérebro lembrar das coisas. E o cortisol tá me matando há 5 anos.\"",
        hookVisual_en="VISUAL HOOK (AI Animated 3D Pixar-Style): BDNF personified — small ball-shaped 'brain fertilizer' creature, glowing bright when healthy. Now grayed out, weak, coughing. Around her, neurons (Pixar style) wither. Cortisol villain (continuity from AD#9, #10, #30, #32) laughs in background. BDNF reaches a feeble hand toward viewer.",
        hookVisual_pt="VISUAL HOOK (Animação 3D AI Pixar-Style): BDNF personificada — pequena criatura em formato de bolinha 'fertilizante cerebral', brilhando intensamente quando saudável. Agora cinza, fraca, tossindo. Ao redor dela, neurônios (estilo Pixar) definham. Cortisol vilão (continuity dos AD#9, #10, #30, #32) ri ao fundo. BDNF estende mão fraca pro espectador.",
        format_en="AI Animated Pixar-Style 3D | Validated internally — entirely new concept per Derick rewrite",
        format_pt="Animação 3D AI Pixar-Style | Validado internamente — conceito inteiramente novo conforme rewrite do Derick",
        speaker_en="BDNF personified (Pixar 3D character) — small fertilizer-creature, shared universe with Cortisol villain",
        speaker_pt="BDNF personificada (personagem Pixar 3D) — pequena criatura-fertilizante, universo compartilhado com Cortisol vilão",
        execution_en="DURATION 2:30. Per Derick: ad horroroso, want completely new idea in Pixar. BDNF as character is original, congruente (LEI #7: Lion's Mane APOIA BDNF, never 'deficiência'), imprevisível. Speaker que ninguém esperava ver hoje. BDNF explains: 'I make your brain plastic. Cortisol is poisoning me.' Lion's Mane arrives as Pixar hero (mushroom-shaped) → revives BDNF. Ashwagandha cuts cortisol. TMC = the team. CTA with 'they'll'.",
        execution_pt="DURAÇÃO 2:30. Conforme Derick: ad horroroso, quer ideia completamente nova em Pixar. BDNF como personagem é original, congruente (LEI #7: Lion's Mane APOIA BDNF, nunca 'deficiência'), imprevisível. Speaker que ninguém esperava ver hoje. BDNF explica: 'Eu deixo seu cérebro plástico. Cortisol tá me envenenando.' Lion's Mane chega como herói Pixar (formato cogumelo) → revive BDNF. Ashwagandha corta cortisol. TMC = a equipe. CTA com 'they'll'.",
    ),

    # AD #57 — TMCAD-215 — Hook A approved + Nurse-in-car format (NOT too long)
    57: dict(
        angle_en="Hook A kept + execution as nurse recording in his car (VH-004 validated) — speaker imprevisível (not doctor — nurse)",
        angle_pt="Hook A mantido + execução como enfermeiro gravando no carro (VH-004 validado) — speaker imprevisível (não doutor — enfermeiro)",
        hookCopy_en="\"You're probably taking ashwagandha. And as a nurse, I can tell you — you're probably taking it wrong.\"",
        hookCopy_pt="\"Você provavelmente tá tomando ashwagandha. E como enfermeiro, eu te digo — você provavelmente tá tomando errado.\"",
        hookVisual_en="VISUAL HOOK (Doctor-in-Car format VH-004 validated, but it's a NURSE not a doctor — imprevisibility): Male nurse 38-45 in scrubs, hospital ID badge visible, drives into the frame, gets into car, closes door, throws his work bag onto passenger seat, exhales heavily, looks at camera (selfie mode mounted on dashboard). Hospital parking lot visible through windshield.",
        hookVisual_pt="VISUAL HOOK (Formato Doctor-in-Car VH-004 validado, mas é um ENFERMEIRO não doutor — imprevisibilidade): Enfermeiro masculino 38-45 de scrubs, crachá hospitalar visível, entra no quadro, senta no carro, fecha a porta, joga maleta no banco do passageiro, exala pesadamente, olha pra câmera (selfie mode montado no painel). Estacionamento do hospital visível pelo parabrisa.",
        format_en="VH-004 (Nurse-in-Car Recording) | Speaker: Male RN 38-45 in scrubs | NOT too long: 90s per Derick",
        format_pt="VH-004 (Gravação Enfermeiro no Carro) | Speaker: Enfermeiro masculino 38-45 de scrubs | NÃO muito longo: 90s conforme Derick",
        speaker_en="Male nurse (RN), 38-45, in scrubs, ID badge visible, in driver's seat at hospital parking lot",
        speaker_pt="Enfermeiro masculino (RN), 38-45, de scrubs, crachá visível, no banco do motorista no estacionamento do hospital",
        execution_en="DURATION 90s (per Derick: not too long). VH-004 validated. Nurse = medical authority + congruence (sees patients) + imprevisibility (not a doctor — who expects a NURSE talking about supplements?). Nurse explains: sees patients with chronic brain fog taking ashwagandha wrong constantly. Most don't use KSM-66 (studied form), dose is always off. 'You need 600mg KSM-66. Most products give you 50mg of root powder.' Recommends TMC. CTA with 'they'll' (specialist pronoun, LEI #4).",
        execution_pt="DURAÇÃO 90s (conforme Derick: não muito longo). VH-004 validado. Enfermeiro = autoridade médica + congruência (vê pacientes) + imprevisibilidade (não é doutor — quem espera ENFERMEIRO falando de suplemento?). Enfermeiro explica: vê pacientes com brain fog crônico tomando ashwagandha errado o tempo todo. Maioria não usa KSM-66 (forma estudada), dose sempre fora. 'Precisa de 600mg KSM-66. Maioria dos produtos dá 50mg de root powder.' Recomenda TMC. CTA com 'they'll' (pronome especialista, LEI #4).",
    ),

    # AD #58 — TMCAD-216 — Hook C kept + Pixar Ashwagandha character + 2:30
    58: dict(
        angle_en="Hook C kept + Ashwagandha personified as Pixar self-aware ingredient — duration reduced to 2:30 per Derick",
        angle_pt="Hook C mantido + Ashwagandha personificada como ingrediente self-aware Pixar — duração reduzida pra 2:30 conforme Derick",
        hookCopy_en="\"If you're taking ashwagandha for brain fog, there's a 90% chance you're wasting your money. Hi, I'm ashwagandha. Let me explain.\"",
        hookCopy_pt="\"Se você tá tomando ashwagandha pra brain fog, 90% de chance de você tá desperdiçando dinheiro. Oi, eu sou ashwagandha. Deixa eu explicar.\"",
        hookVisual_en="VISUAL HOOK (AI Animated 3D Pixar-Style): Ashwagandha personified — curious, friendly Indian-style root character with light Indian accent (Pixar humor). Looks at viewer, irritated, hands on hips: \"90% of you are wasting your money on me. Let me explain.\" Surrounded by chaotic shelf of bad ashwagandha products (low-dose, root powder, wrong forms).",
        hookVisual_pt="VISUAL HOOK (Animação 3D AI Pixar-Style): Ashwagandha personificada — personagem raiz curiosa e simpática com leve sotaque indiano (humor Pixar). Olha pro espectador, irritada, mãos na cintura: \"90% de vocês tá desperdiçando dinheiro comigo. Deixa eu explicar.\" Cercada por estante caótica de produtos ruins de ashwagandha (low-dose, root powder, formas erradas).",
        format_en="AI Animated Pixar-Style 3D | Speaker: Ashwagandha self-aware character | Duration 2:30 (per Derick — reduced from 5:00)",
        format_pt="Animação 3D AI Pixar-Style | Speaker: Ashwagandha personagem self-aware | Duração 2:30 (conforme Derick — reduzido de 5:00)",
        speaker_en="Ashwagandha personified (Pixar 3D character) — curious self-aware ingredient with light Indian accent (Pixar humor)",
        speaker_pt="Ashwagandha personificada (personagem Pixar 3D) — ingrediente curioso self-aware com leve sotaque indiano (humor Pixar)",
        execution_en="DURATION 2:30 (per Derick: between 2-3min, reduced from 5:00). Hook C kept (Derick approved). Speaker IMPREVISÍVEL (ingredient itself talking) + congruente. Self-aware: explains the 4 problems with most ashwagandha products (dosing / timing / form / stacking). 'Most companies use root powder, not KSM-66. That's like drinking dirty water and calling it espresso.' TMC has KSM-66 at clinical dose + Lion's Mane + 10 others. CTA with 'they'll'.",
        execution_pt="DURAÇÃO 2:30 (conforme Derick: entre 2-3min, reduzido de 5:00). Hook C mantido (Derick aprovou). Speaker IMPREVISÍVEL (ingrediente em si falando) + congruente. Self-aware: explica os 4 problemas com a maioria dos produtos de ashwagandha (dose / timing / forma / stacking). 'Maioria das empresas usa root powder, não KSM-66. É tipo beber água suja e chamar de expresso.' TMC tem KSM-66 na dose clínica + Lion's Mane + 10 outros. CTA com 'they'll'.",
    ),

    # AD #59 — TMCRMKT-34 — Total rewrite: 5 signs brain shrinking from cortisol (voice-criteria literal)
    59: dict(
        angle_en="VOICE-CRITERIA NA VEIA per Derick — 5 specific behavioral signs + Disgusting POV visual + ingredient reveal",
        angle_pt="VOICE-CRITERIA NA VEIA conforme Derick — 5 sinais comportamentais específicos + visual Disgusting POV + revela ingrediente",
        hookCopy_en="\"5 signs your brain is shrinking from cortisol — and the one ingredient that's already in your kitchen that stops it.\"",
        hookCopy_pt="\"5 sinais de que seu cérebro está encolhendo por causa do cortisol — e o ingrediente que já está na sua cozinha que para isso.\"",
        hookVisual_en="VISUAL HOOK (Disgusting POV — Derick favorite V-2 #6, voice-criteria literal): Speaker reacts to side-by-side image: hippocampus of healthy 25yo brain vs hippocampus of 50yo brain with chronic cortisol exposure (real medical imaging timelapse, NOT CGI per V-5). Speaker points at screen with disgust: \"THIS is what's happening to YOUR brain RIGHT NOW.\" Suburban dad type at home kitchen.",
        hookVisual_pt="VISUAL HOOK (Disgusting POV — favorito Derick V-2 #6, voice-criteria literal): Speaker reage a imagem side-by-side: hipocampo de cérebro saudável de 25 anos vs hipocampo de cérebro de 50 anos com exposição crônica a cortisol (timelapse de imagem médica real, NÃO CGI conforme V-5). Speaker aponta pra tela com nojo: \"ISSO é o que está acontecendo com SEU cérebro AGORA.\" Tipo pai suburbano na cozinha de casa.",
        format_en="UGC Talking Head + Disgusting POV insert | RTG Video | Speaker: Male 50-58, suburban dad, home kitchen | 60s",
        format_pt="UGC Talking Head + insert Disgusting POV | RTG Video | Speaker: Masculino 50-58, pai suburbano, cozinha de casa | 60s",
        speaker_en="Male 50-58, suburban dad type, in home kitchen — relatable everyman",
        speaker_pt="Masculino 50-58, tipo pai suburbano, cozinha de casa — everyman relacionável",
        execution_en="DURATION 60s. VOICE-CRITERIA APLICADO LITERAL per Derick: ✅ H-1 point-of-pain ESPECÍFICO (5 behaviors concretos) ✅ H-4 2 arcos (5 signs + ingredient) ✅ V-2 Disgusting POV (Derick favorite) ✅ V-1 Efeito WTF (imagem chocante + 5 sintomas escalando) ✅ V-4 ação primeiro frame (reagindo) ✅ LEI #7 BDNF como mecanismo (não 'deficiência de Lion's Mane'). 5 specific signs: forgetting names mid-conversation / rereading emails / walking into rooms forgot why / losing the word / can't focus past 20 min. Brief mechanism: cortisol → BDNF suppression → hippocampus shrinks. TMC has ashwagandha (cortisol cut) + Lion's Mane (BDNF support). CTA with 'we'll' (brand voice, LEI #4).",
        execution_pt="DURAÇÃO 60s. VOICE-CRITERIA APLICADO LITERAL conforme Derick: ✅ H-1 point-of-pain ESPECÍFICO (5 behaviors concretos) ✅ H-4 2 arcos (5 signs + ingrediente) ✅ V-2 Disgusting POV (favorito Derick) ✅ V-1 Efeito WTF (imagem chocante + 5 sintomas escalando) ✅ V-4 ação primeiro frame (reagindo) ✅ LEI #7 BDNF como mecanismo (não 'deficiência de Lion's Mane'). 5 sinais específicos: esquecer nomes no meio da conversa / reler e-mails / entrar em quartos esqueceu por quê / perder a palavra / não foca passa 20 min. Mecanismo breve: cortisol → supressão BDNF → hipocampo encolhe. TMC tem ashwagandha (corte cortisol) + Lion's Mane (suporte BDNF). CTA com 'we'll' (brand voice, LEI #4).",
    ),

}

# ═══════════════════════════════════════════════════════════════
# PATCHING LOGIC
# ═══════════════════════════════════════════════════════════════

def escape_js(s):
    """Escape for JS string (double-quote delimited)."""
    return s.replace('\\', '\\\\').replace('"', '\\"').replace('\n', ' ')

def patch_field(js_block, field, new_value):
    """Replace field:"...", pattern in a JS object string.

    Regex matches a JS double-quoted string with escape sequences:
    - [^"\\]  → any char that's not " or \
    - \\.     → backslash followed by any char (escape sequence)
    """
    pattern = rf'{re.escape(field)}:"(?:[^"\\]|\\.)*"'
    replacement = f'{field}:"{escape_js(new_value)}"'
    result, n = re.subn(pattern, replacement, js_block)
    if n == 0:
        print(f"  WARNING: field '{field}' not found in ad block")
    return result

def add_version_field(js_block, version=2):
    """Add v:N field to a JS ad object before closing }."""
    if re.search(r',v:\d+', js_block):
        # already has v:, update it
        return re.sub(r',v:\d+', f',v:{version}', js_block)
    # else inject before closing }
    return js_block[:-1] + f',v:{version}' + js_block[-1]

# Extract ADS array bounds
ads_start = html.find('const ADS = [')
ads_end = html.find('];', ads_start) + 2
ads_js = html[ads_start:ads_end]

# Parse individual ad objects
ad_objects = []
pattern = re.compile(r'(\{id:(\d+),.*?\})', re.DOTALL)
for m in pattern.finditer(ads_js):
    ad_objects.append((m.start(), m.end(), int(m.group(2)), m.group(1)))

patched_ads_js = ads_js
offset = 0
patched_count = 0

for orig_start, orig_end, ad_id, orig_block in ad_objects:
    if ad_id not in UPDATES:
        continue

    print(f"Patching ad id={ad_id}...")
    new_block = orig_block
    for field, value in UPDATES[ad_id].items():
        new_block = patch_field(new_block, field, value)

    # Stamp version
    new_block = add_version_field(new_block, version=2)

    abs_start = orig_start + offset
    abs_end = orig_end + offset
    patched_ads_js = patched_ads_js[:abs_start] + new_block + patched_ads_js[abs_end:]
    offset += len(new_block) - (orig_end - orig_start)
    patched_count += 1

# Reconstruct full HTML
new_html = html[:ads_start] + patched_ads_js + html[ads_end:]

# ═══════════════════════════════════════════════════════════════
# INJECT VERSION-AWARE STATE MIGRATION
# ═══════════════════════════════════════════════════════════════

OLD_LOAD = "function loadState() { try { const r = localStorage.getItem(STORAGE_KEY); return r ? JSON.parse(r) : {}; } catch(e) { return {}; } }"
OLD_SAVE = "function saveState() { localStorage.setItem(STORAGE_KEY, JSON.stringify(state)); updateStats(); renderDayTabs(); }"

NEW_LOAD = (
    "function loadState() { "
    "try { "
    "const r = localStorage.getItem(STORAGE_KEY); "
    "if (!r) return {}; "
    "const raw = JSON.parse(r); "
    "const migrated = {}; "
    "ADS.forEach(ad => { "
    "const adV = ad.v || 1; "
    "const savedV = (raw[ad.id] && raw[ad.id].v) || 1; "
    "if (raw[ad.id] && savedV === adV) migrated[ad.id] = raw[ad.id]; "
    "}); "
    "return migrated; "
    "} catch(e) { return {}; } "
    "}"
)

NEW_SAVE = (
    "function saveState() { "
    "ADS.forEach(ad => { "
    "if (state[ad.id]) state[ad.id].v = ad.v || 1; "
    "}); "
    "localStorage.setItem(STORAGE_KEY, JSON.stringify(state)); "
    "updateStats(); "
    "renderDayTabs(); "
    "}"
)

if OLD_LOAD in new_html:
    new_html = new_html.replace(OLD_LOAD, NEW_LOAD)
    print("✓ loadState() migration logic injected")
else:
    print("⚠ WARNING: loadState() not found in original form")

if OLD_SAVE in new_html:
    new_html = new_html.replace(OLD_SAVE, NEW_SAVE)
    print("✓ saveState() versioning injected")
else:
    print("⚠ WARNING: saveState() not found in original form")

# ═══════════════════════════════════════════════════════════════
# CONTENT-VERSION META TAG (for curl deploy verification)
# ═══════════════════════════════════════════════════════════════

if 'name="content-version"' in new_html:
    new_html = re.sub(
        r'<meta name="content-version" content="[^"]*">',
        f'<meta name="content-version" content="{VERSION_TAG}">',
        new_html,
        count=1
    )
    print(f"✓ content-version meta updated to {VERSION_TAG}")
else:
    # Inject after existing meta viewport
    new_html = new_html.replace(
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        f'<meta name="viewport" content="width=device-width, initial-scale=1">\n<meta name="content-version" content="{VERSION_TAG}">',
        1
    )
    print(f"✓ content-version meta injected: {VERSION_TAG}")

# ═══════════════════════════════════════════════════════════════
# WRITE OUT
# ═══════════════════════════════════════════════════════════════

HTML_PATH.write_text(new_html)
print(f"\n✅ Done. {patched_count} ads patched (expected 32).")
print(f"   Content-version: {VERSION_TAG}")
print(f"   File: {HTML_PATH}")
