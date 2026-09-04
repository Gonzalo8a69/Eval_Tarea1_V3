def validar_ipr(pr, pb, j, pwf):
    if any(v < 0 for v in [pr, pb, j, pwf]): return False, "**Los Parámetros no pueden ser negativos.**"
    if pr <= pb: return False, "Pr debe ser mayor a Pb."
    if pwf > pr: return False, "Pwf no puede superar Pr."
    return True, "OK"

def validar_perforacion(mw, md, tvd, pform):
    if mw <= 0 or md <= 0 or tvd <= 0: return False, "** Los Parámetros MW, MD y TVD deben ser > 0.**"
    if pform < 0: return False, "**La Presión de formación no puede ser negativa.**"
    if tvd > md: return False, "**La profundidad en TVD no puede ser mayor a la profundidad en MD.**"
    return True, "OK"

def validar_poes(area, h, ntg, porosidad, swi, boi, fr):
    if area <= 0 or h <= 0: return False, "** El Área y Espesor deben ser > 0.**"
    if not all(0 <= val <= 1 for val in [ntg, porosidad, swi, fr]): return False, "**Los valores de NTG, Porosidad, Swi y FR deben ser fracciones.**"
    if boi <= 0: return False, "Boi debe ser > 0."
    return True, "OK"
