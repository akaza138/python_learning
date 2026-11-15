class employee():
    comp_name="google"
    @classmethod
    def change_comp(cls,new_name):
        cls.comp_name=new_name

employee.change_comp("open Ai")
print(employee.comp_name)