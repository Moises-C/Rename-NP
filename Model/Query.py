
class Query:
    
    @staticmethod
    def custom_declare():
        return """ 
        SELECT num_refe 
        FROM SAAIO_PEDIME
        WHERE SAAIO_PEDIME.DIA_PAGO >= '2026-01-01'
            AND SAAIO_PEDIME.FIR_PAGO IS NOT null
            AND SAAIO_PEDIME.FIR_ELEC IS NOT NULL
            AND SAAIO_PEDIME.CVE_IMPO = '3273'
        """
        