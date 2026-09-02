def validar_ipr(pr, pb, j, pwf):
    if any(v < 0 for v in [pr, pb, j, pwf]): return False, "Parámetros no pueden ser negativos."
    if pr <= pb: return False, "Pr debe ser mayor a Pb."
    if pwf > pr: return False, "Pwf no puede superar Pr."
    return True, "OK"

def validar_perforacion(mw, md, tvd, pform):
    if mw <= 0 or md <= 0 or tvd <= 0: return False, "MW, MD y TVD deben ser > 0."
    if pform < 0: return False, "Presión de formación no puede ser negativa."
    if tvd > md: return False, "TVD no puede ser mayor a MD."
    return True, "OK"

def validar_poes(area, h, ntg, porosidad, swi, boi, fr):
    if area <= 0 or h <= 0: return False, "Área y espesor deben ser > 0."
    if not all(0 <= val <= 1 for val in [ntg, porosidad, swi, fr]): return False, "NTG, Porosidad, Swi y FR deben ser fracciones."
    if boi <= 0: return False, "Boi debe ser > 0."
    return True, "OK"