class brojError(Exception):
    def __init__(self,code):
        self.error_message=''
        self.error_dict={
            000: "ERROR 000: Nespecificirana pogreška",
            101: "ERROR 101: Pogrešan unos, pokušajte ponovno."
            }
        try:
            self.error_message+=self.error_dict[code]
        except KeyError:
            self.error_message += self.error_dict[000]