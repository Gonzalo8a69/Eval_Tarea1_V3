from dataclasses import dataclass

@dataclass
class ReservorioSubsaturado:
    pr: float
    pb: float
    j: float

@dataclass
class DatosPozo:
    mw: float
    md: float
    tvd: float
    pform: float

@dataclass
class PropiedadesPetrofisicas:
    area: float
    h: float
    ntg: float
    porosidad: float
    swi: float
    boi: float
    fr: float