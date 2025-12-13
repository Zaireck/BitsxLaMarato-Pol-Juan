class PredicionInfo:

    def __init__(   
                    self,  
                    recept_est_porcent,
                    tipo_histologico,
                    Grado,
                    ecotv_infiltobj,
                    ecotv_infiltsub,
                    estadiaje_pre_i,
                    grupo_riesgo,
                    asa,
                    afectacion_linf,
                    AP_ganPelv,
                    AP_glanPaor,
                    beta_cateninap,
                    estadificacion_,
                    FIGO2023,
                    grupo_de_riesgo_definitivo,
                    rdt,
                    recep_est_porcent_medido,
                    tamano_tumoral_medido,
                    recep_est_porcent,
                    tamano_tumoral
                ):
        
        self.__recept_est_porcent = recept_est_porcent
        self.__tipo_histologico = tipo_histologico
        self.__Grado = Grado
        self.__ecotv_infiltobj = ecotv_infiltobj
        self.__ecotv_infiltsub = ecotv_infiltsub
        self.__estadiaje_pre_i = estadiaje_pre_i
        self.__grupo_riesgo = grupo_riesgo
        self.__asa = asa
        self.__afectacion_linf = afectacion_linf
        self.__AP_ganPelv = AP_ganPelv
        self.__AP_glanPaor = AP_glanPaor
        self.__beta_cateninap = beta_cateninap
        self.__estadificacion_ = estadificacion_
        self.__FIGO2023 = FIGO2023
        self.__grupo_de_riesgo_definitivo = grupo_de_riesgo_definitivo
        self.__rdt = rdt
        self.__recep_est_porcent_medido = recep_est_porcent_medido
        self.__tamano_tumoral_medido = tamano_tumoral_medido
        self.__recep_est_porcent = recep_est_porcent
        self.__tamano_tumoral = tamano_tumoral

    @property
    def recept_est_porcent(self):
        return self.__recept_est_porcent

    @recept_est_porcent.setter
    def recept_est_porcent(self, value):
        self.__recept_est_porcent = value

    @property
    def tipo_histologico(self):
        return self.__tipo_histologico

    @tipo_histologico.setter
    def tipo_histologico(self, value):
        self.__tipo_histologico = value

    @property
    def Grado(self):
        return self.__Grado

    @Grado.setter
    def Grado(self, value):
        self.__Grado = value

    @property
    def ecotv_infiltobj(self):
        return self.__ecotv_infiltobj
    
    @ecotv_infiltobj.setter
    def ecotv_infiltobj(self, value):
        self.__ecotv_infiltobj = value

    @property
    def ecotv_infiltsub(self):
        return self.__ecotv_infiltsub
    
    @ecotv_infiltsub.setter
    def ecotv_infiltsub(self, value):
        self.__ecotv_infiltsub = value

    @property
    def estadiaje_pre_i(self):
        return self.__estadiaje_pre_i
    
    @estadiaje_pre_i.setter
    def estadiaje_pre_i(self, value):
        self.__estadiaje_pre_i = value

    @property
    def grupo_riesgo(self):
        return self.__grupo_riesgo
    
    @grupo_riesgo.setter
    def grupo_riesgo(self, value):
        self.__grupo_riesgo = value

    @property
    def asa(self):
        return self.__asa
    
    @asa.setter
    def asa(self, value):
        self.__asa = value

    @property
    def afectacion_linf(self):
        return self.__afectacion_linf
    
    @afectacion_linf.setter
    def afectacion_linf(self, value):
        self.__afectacion_linf = value

    @property
    def AP_ganPelv(self):
        return self.__AP_ganPelv
    
    @AP_ganPelv.setter
    def AP_ganPelv(self, value):
        self.__AP_ganPelv = value

    @property
    def AP_glanPaor(self):
        return self.__AP_glanPaor

    @AP_glanPaor.setter
    def AP_glanPaor(self, value):
        self.__AP_glanPaor = value

    @property
    def beta_cateninap(self):
        return self.__beta_cateninap

    @beta_cateninap.setter
    def beta_cateninap(self, value):
        self.__beta_cateninap = value

    @property
    def estadificacion_(self):
        return self.__estadificacion_

    @estadificacion_.setter
    def estadificacion_(self, value):
        self.__estadificacion_ = value

    @property
    def FIGO2023(self):
        return self.__FIGO2023

    @FIGO2023.setter
    def FIGO2023(self, value):
        self.__FIGO2023 = value

    @property
    def grupo_de_riesgo_definitivo(self):
        return self.__grupo_de_riesgo_definitivo

    @grupo_de_riesgo_definitivo.setter
    def grupo_de_riesgo_definitivo(self, value):
        self.__grupo_de_riesgo_definitivo = value

    @property
    def rdt(self):
        return self.__rdt

    @rdt.setter
    def rdt(self, value):
        self.__rdt = value

    @property
    def recep_est_porcent_medido(self):
        return self.__recep_est_porcent_medido
    
    @recep_est_porcent_medido.setter
    def recep_est_porcent_medido(self, value):
        self.__recep_est_porcent_medido = value

    @property
    def tamano_tumoral_medido(self):
        return self.__tamano_tumoral_medido
    
    @tamano_tumoral_medido.setter
    def tamano_tumoral_medido(self, value):
        self.__tamano_tumoral_medido = value

    @property
    def recep_est_porcent(self):
        return self.__recep_est_porcent
    
    @recep_est_porcent.setter
    def recep_est_porcent(self, value):
        self.__recep_est_porcent = value

    @property
    def tamano_tumoral(self):
        return self.__tamano_tumoral        
    
    @tamano_tumoral.setter
    def tamano_tumoral(self, value):
        self.__tamano_tumoral = value