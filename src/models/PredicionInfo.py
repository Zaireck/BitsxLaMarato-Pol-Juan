class PredicionInfo:

    def __init__(self):
        #TODO: Todos a none
        self._repository = None
        pass

    def __init__(self, repository):
        #TODO: Todos a sus respectivos valores - Añadir atributos relevantes
        self._repository = repository
        pass

    #TODO: Añadir getters y setters a todos los atributos
    @property #Getter
    def repository(self):
        return self._repository

    @repository.setter #Setter
    def repository(self, repo):
        self._repository = repo