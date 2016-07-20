def param_is_primitives(sig_line):
    pass

def param_is_dataStructs(sig_line):
    pass

def prim_types(sig_line):
    pass

def check_structs(sig_lines,file_obj):
    pass





class InputCLass(object):
    prims = []
    data_structs = []
    def __init__(self,signature,fileDirctory):
        self.sig = signature
        self.fid = fileDirctory
        print(self.sig)
        print(self.fid)


    def the_inputs(self):
        if param_is_primitives(self.sig) or param_is_dataStructs(self.sig):
            InputCLass.prims = prim_types(self.sig)
            InputCLass.data_structs= check_structs(self.sig,self,file_dirctory)
            return [prims,data_structs]
        return "no input"
    
    def get_fid(self):
        return self.fid

    def get_sig(self):
        return self.si

    def set_sig(self, in_sig):
        self.sig = in_sig

    def set_fid(self ,in_fid):
        self.fid = in_fid


