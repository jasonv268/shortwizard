class Basique:
    def __init__(self, volume=1.0, fondu_entree=0, fondu_sortie=0) -> None:
        self.volume = volume
        self.fondu_entree = fondu_entree
        self.fondu_sortie = fondu_sortie


default = Basique()