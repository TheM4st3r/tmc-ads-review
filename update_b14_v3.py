#!/usr/bin/env python3
"""
Update B14 review (v3) — apply 8 corrections from review feedback 2026-05-06.

Changes:
- Technical (4): #10 duration 3:30→2:30 / #21 2:40→2:00 / #32 2:30→2:00 / #44 Boron→Zinc
- Flag (1):     #22 "Derick is writing this one"
- Creative (3): #33 Dramatic Presentation 2 speakers / #34 Contrarian Use pre-workout trash / #46 Contrarian Use L-citrulline drain

Per-ad versioning bump to v:3 — modified ads return to pending,
previously-approved-after-v2 ads keep their state.
"""

import re
import datetime
from pathlib import Path

HTML_PATH = Path("/tmp/tmc-ads-review/index.html")
html = HTML_PATH.read_text()

TODAY = datetime.date.today().strftime('%Y-%m-%d')
VERSION_TAG = f"B14-corrected-v3-{TODAY}"

# ═══════════════════════════════════════════════════════════════
# UPDATES — only fields that change for each ad
# ═══════════════════════════════════════════════════════════════

UPDATES = {

    # ──────────────────────────────────────────────────
    # AD #10 — duration 3:30 → 2:30 (Cortisol Vilão LONG)
    # ──────────────────────────────────────────────────
    10: dict(
        format_en="AI Animated Pixar-Style 3D — Mini-VSL narrative (2:30)",
        format_pt="Animação 3D AI Pixar-Style — Mini-VSL narrativo (2:30)",
        execution_en="DURATION 2:30 (per Derick v2 feedback — reduced from 3:30). Cross-cluster bridge (1 hormone, 3 symptoms) executed via epic Pixar storytelling. Cortisol narrates his takeover with sarcastic humor (Mr. Burns vibe). Shows cascading damage to energy/recovery/focus. Then heroes arrive: ashwagandha (suit-wearing fixer), tongkat ali, Lion's Mane. They liberate the control room. CTA with 'they'll' (mascot, LEI #4). Entertainment-first DR. Cumpre 'ad inteiro nativamente curioso'.",
        execution_pt="DURAÇÃO 2:30 (conforme feedback v2 do Derick — reduzido de 3:30). Bridge cross-cluster (1 hormônio, 3 sintomas) executado via storytelling Pixar épico. Cortisol narra sua tomada de poder com humor sarcástico (vibe Mr. Burns). Mostra dano em cascata em energia/recovery/foco. Heróis chegam: ashwagandha (consertador de terno), tongkat ali, Lion's Mane. Eles libertam a sala de controle. CTA com 'they'll' (mascote, LEI #4).",
    ),

    # ──────────────────────────────────────────────────
    # AD #21 — duration 2:40 → 2:00 (T Encolhendo Ao Vivo)
    # ──────────────────────────────────────────────────
    21: dict(
        execution_en="DURATION 2:00 (per Derick v2 feedback — reduced from 2:40). Structure: \"Hi, I'm your [X]\" + visual transformation. T explains the cascade: SHBG traps her, cortisol suppresses production, dopamine signaling weakens. \"You're not weaker. I am.\" TMC ingredients (zinc supports T production, tongkat ali boosts it, ashwagandha cuts cortisol) appear as Pixar heroes restoring T to glory at end. Speaker IMPREVISÍVEL (T encolhendo ao vivo), congruente (cluster muscle/recovery). CTA with 'they'll'.",
        execution_pt="DURAÇÃO 2:00 (conforme feedback v2 do Derick — reduzido de 2:40). Estrutura: \"Oi, eu sou sua [X]\" + transformação visual. T explica a cascata: SHBG aprisiona ela, cortisol suprime produção, sinalização dopamina enfraquece. \"Você não está mais fraco. Eu estou.\" Ingredientes TMC (zinco suporta produção T, tongkat ali aumenta, ashwagandha corta cortisol) aparecem como heróis Pixar restaurando T à glória no final. Speaker IMPREVISÍVEL (T encolhendo ao vivo), congruente. CTA com 'they'll'.",
    ),

    # ──────────────────────────────────────────────────
    # AD #22 — Derick is writing this one (FLAG)
    # ──────────────────────────────────────────────────
    22: dict(
        angle_en="[DERICK IS WRITING THIS ONE — pipeline does not produce script. Original concept rejected v2: 'Coisa horrorosa.']",
        angle_pt="[DERICK ESTÁ ESCREVENDO ESSE — pipeline não produz o script. Conceito original rejeitado v2: 'Coisa horrorosa.']",
        hookCopy_en="[DERICK WRITES — placeholder]",
        hookCopy_pt="[DERICK ESCREVE — placeholder]",
        hookVisual_en="[DERICK WRITES — placeholder]",
        hookVisual_pt="[DERICK ESCREVE — placeholder]",
        format_en="[DERICK WRITES THIS ONE]",
        format_pt="[DERICK ESCREVE ESSE]",
        speaker_en="[DERICK WRITES]",
        speaker_pt="[DERICK ESCREVE]",
        execution_en="[DERICK WRITES THIS ONE — pipeline does not produce script. Skip in agente-escrita.]",
        execution_pt="[DERICK ESCREVE ESSE — pipeline não produz o script. Pular no agente-escrita.]",
    ),

    # ──────────────────────────────────────────────────
    # AD #32 — duration 2:30 → 2:00 (Cortisol confessor MID)
    # ──────────────────────────────────────────────────
    32: dict(
        format_en="AI Animated Pixar-Style 3D — Pixar villain monologue (2:00)",
        format_pt="Animação 3D AI Pixar-Style — monólogo vilão Pixar (2:00)",
        execution_en="DURATION 2:00 (per Derick v2 feedback — reduced from 2:30). Pixar villain narrating his own crimes = pure entertainment with embedded education. Cortisol explains step-by-step how he sabotages: blocks T production, hijacks dopamine, fragments sleep, drains adrenals. TMC heroes (ashwagandha primary) arrive at end and put him in handcuffs. Imprevisível, congruente, multi-loop. CTA with 'they'll'.",
        execution_pt="DURAÇÃO 2:00 (conforme feedback v2 do Derick — reduzido de 2:30). Vilão Pixar narrando suas próprias crimes = entretenimento puro com educação embutida. Cortisol explica passo a passo como ele sabota: bloqueia produção T, sequestra dopamina, fragmenta sono, drena adrenais. Heróis TMC (ashwagandha principal) chegam no final e o algemam. Imprevisível, congruente, multi-loop. CTA com 'they'll'.",
    ),

    # ──────────────────────────────────────────────────
    # AD #33 — Dramatic Presentation 2 speakers (1:30) — Opção A APROVADA
    # ──────────────────────────────────────────────────
    33: dict(
        angle_en="Lost gym drive is biology, not character — Dramatic Presentation with 2 speakers (fit + sedentary) makes it visual",
        angle_pt="Drive perdido é biologia, não caráter — Dramatic Presentation com 2 speakers (fit + sedentário) torna isso visual",
        hookCopy_en="\"Look at this man. He WANTS to go. His body says no. His testosterone is 287 and his cortisol is at 8 PM levels at 7 AM. Until you fix that — the couch wins every time.\"",
        hookCopy_pt="\"Olha pra esse homem. Ele QUER ir. O corpo dele diz não. Testosterona dele tá em 287 e o cortisol tá em níveis de 8 da noite às 7 da manhã. Até você consertar isso — o sofá vence sempre.\"",
        hookVisual_en="VISUAL HOOK (Dramatic Presentation, V-2 #5 — Derick favorite): Speaker A (fit 50+, atlético, breathing slightly heavy) walks into another man's living room. Speaker B (same age, gut, exhausted, in workout clothes but on couch). Speaker A grabs Speaker B's arm and tries to pull him off the couch — Speaker B doesn't budge, doesn't even resist, just sits. Speaker A turns to camera and points at Speaker B with the other hand still holding Speaker B's arm.",
        hookVisual_pt="VISUAL HOOK (Dramatic Presentation, V-2 #5 — favorito Derick): Speaker A (fit 50+, atlético, respirando levemente pesado) entra na sala de outro homem. Speaker B (mesma idade, gut, exausto, com roupas de academia mas no sofá). Speaker A pega o braço do Speaker B e tenta puxar do sofá — Speaker B não cede, nem resiste, só fica sentado. Speaker A vira pra câmera e aponta pro Speaker B com a outra mão ainda segurando o braço dele.",
        format_en="UGC Dramatic Presentation with 2 speakers (VH-001 variation) | Duration 1:30",
        format_pt="UGC Dramatic Presentation com 2 speakers (variação VH-001) | Duração 1:30",
        speaker_en="Speaker A: fit 50yo male, atlético, addressing camera | Speaker B: same age, sedentary, on couch (non-speaking but visible throughout)",
        speaker_pt="Speaker A: masculino fit 50yo, atlético, dirigindo-se à câmera | Speaker B: mesma idade, sedentário, no sofá (sem falas mas visível durante todo o ad)",
        execution_en="DURATION 1:30 (per Derick v2 feedback). Voice-criteria archetype: Dramatic Presentation (V-2 #5, Derick favorite — \"If [body looks like this]\" pattern). 2 speakers = imprevisibility extreme + congruência elite. Speaker A delivers hook with point-of-pain SPECIFIC numbers (T 287, cortisol 8pm at 7am). Quick mechanism explained directly: \"Cortisol blocks dopamine reward signaling. Without dopamine, your brain can't generate the 'want' for the gym.\" TMC = ashwagandha cuts cortisol + tongkat ali T support + zinc. Visual proof: Speaker A drinks TMC, hands cup to Speaker B who sips and gets up after 5 seconds. CTA with 'they'll' (UGC).",
        execution_pt="DURAÇÃO 1:30 (conforme feedback v2 do Derick). Voice-criteria archetype: Dramatic Presentation (V-2 #5, favorito Derick — padrão \"If [body looks like this]\"). 2 speakers = imprevisibilidade extrema + congruência elite. Speaker A entrega hook com números point-of-pain ESPECÍFICOS (T 287, cortisol 8pm às 7am). Mecanismo rápido explicado diretamente: \"Cortisol bloqueia sinalização de reward da dopamina. Sem dopamina, seu cérebro não consegue gerar a 'vontade' pela academia.\" TMC = ashwagandha corta cortisol + tongkat ali suporta T + zinco. Prova visual: Speaker A toma TMC, passa o copo pro Speaker B que dá um gole e levanta depois de 5 segundos. CTA com 'they'll' (UGC).",
    ),

    # ──────────────────────────────────────────────────
    # AD #34 — Contrarian Use pre-workout trash (1:00-1:15) — Opção A APROVADA
    # ──────────────────────────────────────────────────
    34: dict(
        angle_en="Pre-workout is just expensive sugar without testosterone foundation — Contrarian Use shows it visually",
        angle_pt="Pre-workout é só açúcar caro sem foundation de testosterona — Contrarian Use mostra isso visualmente",
        hookCopy_en="\"That pre-workout in your kitchen? Below 350 testosterone, it's expensive sugar.\"",
        hookCopy_pt="\"Aquele pre-workout na sua cozinha? Abaixo de 350 de testosterona, é açúcar caro.\"",
        hookVisual_en="VISUAL HOOK (Contrarian Use, V-2 #2 — Derick favorite #1): Speaker in kitchen scoops out pre-workout powder from a popular branded tub, tastes it (touches tongue), makes disgusted face. Then DUMPS the entire tub into the trash can. Picks up TMC from the counter, looks at camera: \"THIS is what it was missing all along.\"",
        hookVisual_pt="VISUAL HOOK (Contrarian Use, V-2 #2 — favorito Derick #1): Speaker na cozinha pega scoop de pre-workout em pó de um pote de marca popular, prova (encosta na língua), faz cara de nojo. Aí JOGA o pote inteiro no lixo. Pega TMC da bancada, olha pra câmera: \"ISSO é o que ele tava faltando o tempo todo.\"",
        format_en="UGC Talking Head + Contrarian Use visual hook | Duration 1:00-1:15",
        format_pt="UGC Talking Head + Contrarian Use visual hook | Duração 1:00-1:15",
        speaker_en="Male 45-55, kitchen setting, casual, healthy but not extreme physique",
        speaker_pt="Masculino 45-55, cozinha, casual, físico saudável mas não extremo",
        execution_en="DURATION 1:00-1:15 (per Derick v2 feedback — short replaces 3:30 Mini-VSL). Voice-criteria archetype: Contrarian Use (V-2 #2, Derick favorite #1). WTF visual extremo (jogar pre-workout caro NO LIXO) = imprevisibilidade extrema + multi-loop. Imprevisível, congruente (zero drive = needs foundation, not stimulant). Quick mechanism: pre-workout caffeine + L-citrulline does nothing for cortisol-induced dopamine collapse. TMC fixes the foundation (ashwagandha cuts cortisol → dopamine signaling restored). CTA with 'they'll' (UGC).",
        execution_pt="DURAÇÃO 1:00-1:15 (conforme feedback v2 do Derick — curto substitui Mini-VSL de 3:30). Voice-criteria archetype: Contrarian Use (V-2 #2, favorito Derick #1). Visual WTF extremo (jogar pre-workout caro NO LIXO) = imprevisibilidade extrema + multi-loop. Imprevisível, congruente (zero drive = precisa de foundation, não estimulante). Mecanismo rápido: cafeína de pre-workout + L-citrulina não faz nada pro colapso de dopamina induzido por cortisol. TMC consegue a foundation (ashwagandha corta cortisol → sinalização dopamina restaurada). CTA com 'they'll' (UGC).",
    ),

    # ──────────────────────────────────────────────────
    # AD #44 — Boron → Zinc throughout (Mineral That Frees T MID)
    # ──────────────────────────────────────────────────
    44: dict(
        angle_en="Zinc arrives as caped Pixar hero to break T out of SHBG prison — rescue narrative as mechanism reveal",
        angle_pt="Zinco chega como herói Pixar com capa pra quebrar T da prisão SHBG — narrativa de resgate como revelação de mecanismo",
        hookCopy_en="\"Most of your testosterone is locked in a cage. There's one mineral that can break the lock — and you're probably not getting enough of it.\"",
        hookCopy_pt="\"A maior parte da sua testosterona está trancada numa jaula. Existe um mineral que pode quebrar a fechadura — e você provavelmente não está tomando o suficiente.\"",
        hookVisual_en="VISUAL HOOK (AI Animated 3D Pixar-Style): SHBG molecular prison cell. T (defeated, multiple copies) trapped behind bars. Zinc (caped Pixar hero with Zn insignia on chest) walks in dramatic slow-motion, plants himself in front of cell: \"I'm here to break you out.\" Lock cracks. Cinematic Pixar action.",
        hookVisual_pt="VISUAL HOOK (Animação 3D AI Pixar-Style): Cela de prisão molecular SHBG. T (derrotada, múltiplas cópias) presa atrás de barras. Zinco (herói Pixar com capa e insígnia Zn no peito) entra em câmera lenta dramática, se planta na frente da cela: \"Tô aqui pra te tirar.\" Fechadura racha. Ação cinematográfica Pixar.",
        format_en="AI Animated Pixar-Style 3D — rescue narrative (2:30)",
        format_pt="Animação 3D AI Pixar-Style — narrativa de resgate (2:30)",
        speaker_en="Zinc (caped Pixar hero) + Testosterone (rescued character) + SHBG (defeated jailer) — continuity from AD#42",
        speaker_pt="Zinco (herói Pixar com capa) + Testosterona (personagem resgatada) + SHBG (carcereiro derrotado) — continuity do AD#42",
        execution_en="DURATION 2:30. Storytelling de resgate Pixar = curiosidade total. Mechanism (SHBG/Zinc) embedded in visual narrative. T explains: 'I was trapped for years. Then Zinc showed up.' TMC contains zinc + tongkat ali + ashwagandha — the full liberation team. Per Derick v2 feedback: Boron is NOT in TMC formula — replaced with Zinc throughout. CTA with 'they'll'.",
        execution_pt="DURAÇÃO 2:30. Storytelling de resgate Pixar = curiosidade total. Mecanismo (SHBG/Zinco) embutido em narrativa visual. T explica: 'Fiquei presa por anos. Aí Zinco apareceu.' TMC contém zinco + tongkat ali + ashwagandha — a equipe completa de libertação. Conforme feedback v2 do Derick: Boron NÃO está na fórmula do TMC — substituído por Zinco em tudo. CTA com 'they'll'.",
    ),

    # ──────────────────────────────────────────────────
    # AD #46 — Contrarian Use L-citrulline drain (1:00-1:30) — Opção B APROVADA
    # ──────────────────────────────────────────────────
    46: dict(
        angle_en="L-citrulline is wasted without testosterone foundation — Contrarian Use sends supplement money down the drain (literally)",
        angle_pt="L-citrulina é desperdiçada sem foundation de testosterona — Contrarian Use joga o dinheiro do suplemento pelo ralo (literalmente)",
        hookCopy_en="\"That L-citrulline in your kitchen is doing nothing without the foundation underneath it.\"",
        hookCopy_pt="\"Aquela L-citrulina na sua cozinha não tá fazendo nada sem a foundation embaixo.\"",
        hookVisual_en="VISUAL HOOK (Contrarian Use, V-2 #2 — Derick favorite #1): Speaker in kitchen grabs a tub of L-citrulline (popular pre-workout ingredient, branded). \"If your testosterone is below 350, this is the most expensive way to do nothing.\" DUMPS the entire content into the kitchen sink. Turns on faucet. Watches the powder swirl and wash down the drain. Camera holds on the empty tub.",
        hookVisual_pt="VISUAL HOOK (Contrarian Use, V-2 #2 — favorito Derick #1): Speaker na cozinha pega um potão de L-citrulina (ingrediente popular de pre-workout, com marca). \"Se sua testosterona tá abaixo de 350, esse é o jeito mais caro de não fazer nada.\" JOGA o conteúdo inteiro na pia da cozinha. Liga a torneira. Assiste o pó rodopiar e descer pelo ralo. Câmera segura no pote vazio.",
        format_en="UGC Talking Head + Contrarian Use visual hook | Duration 1:00-1:30",
        format_pt="UGC Talking Head + Contrarian Use visual hook | Duração 1:00-1:30",
        speaker_en="Male 50-60, kitchen counter, lifter physique (visible forearms/shoulders)",
        speaker_pt="Masculino 50-60, bancada de cozinha, físico de lifter (antebraços/ombros visíveis)",
        execution_en="DURATION 1:00-1:30 (per Derick v2 feedback — short replaces 3:30 Pixar Mini-VSL épico). Voice-criteria archetype: Contrarian Use (V-2 #2, Derick favorite #1). Visual proof of waste (suplemento caro pelo ralo) = WTF extremo. Imprevisível + congruente (no pump = NO pathway needs T foundation). Quick mechanism: NO production = L-citrulline + endothelial function (T-driven via eNOS). Without T, L-citrulline is just protein for the kidneys. TMC has L-citrulline + tongkat ali + ashwagandha + zinc — the full system. CTA with 'they'll' (UGC).",
        execution_pt="DURAÇÃO 1:00-1:30 (conforme feedback v2 do Derick — curto substitui Pixar Mini-VSL épico de 3:30). Voice-criteria archetype: Contrarian Use (V-2 #2, favorito Derick #1). Prova visual de desperdício (suplemento caro pelo ralo) = WTF extremo. Imprevisível + congruente (no pump = via NO precisa de foundation T). Mecanismo rápido: produção de NO = L-citrulina + função endotelial (T-dirigida via eNOS). Sem T, L-citrulina é só proteína pros rins. TMC tem L-citrulina + tongkat ali + ashwagandha + zinco — o sistema completo. CTA com 'they'll' (UGC).",
    ),

}

# ═══════════════════════════════════════════════════════════════
# PATCHING LOGIC (same as v2 with corrected regex)
# ═══════════════════════════════════════════════════════════════

def escape_js(s):
    return s.replace('\\', '\\\\').replace('"', '\\"').replace('\n', ' ')

def patch_field(js_block, field, new_value):
    pattern = rf'{re.escape(field)}:"(?:[^"\\]|\\.)*"'
    replacement = f'{field}:"{escape_js(new_value)}"'
    result, n = re.subn(pattern, replacement, js_block)
    if n == 0:
        print(f"  WARNING: field '{field}' not found in ad block")
    return result

def set_version_field(js_block, version):
    """Set v:N field to a JS ad object before closing }."""
    if re.search(r',v:\d+', js_block):
        return re.sub(r',v:\d+', f',v:{version}', js_block)
    return js_block[:-1] + f',v:{version}' + js_block[-1]

# Extract ADS array bounds
ads_start = html.find('const ADS = [')
ads_end = html.find('];', ads_start) + 2
ads_js = html[ads_start:ads_end]

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

    # Bump to v:3 — forces this ad back to pending in localStorage
    new_block = set_version_field(new_block, version=3)

    abs_start = orig_start + offset
    abs_end = orig_end + offset
    patched_ads_js = patched_ads_js[:abs_start] + new_block + patched_ads_js[abs_end:]
    offset += len(new_block) - (orig_end - orig_start)
    patched_count += 1

new_html = html[:ads_start] + patched_ads_js + html[ads_end:]

# Update content-version meta
new_html = re.sub(
    r'<meta name="content-version" content="[^"]*">',
    f'<meta name="content-version" content="{VERSION_TAG}">',
    new_html,
    count=1
)
print(f"✓ content-version meta updated to {VERSION_TAG}")

HTML_PATH.write_text(new_html)
print(f"\n✅ Done. {patched_count} ads patched (expected 8).")
print(f"   Content-version: {VERSION_TAG}")
