# TERMINADO
import unittest
from Config.config import login_data, images, csv_files_path
from sge_functions.sge_functions import sge_functions
from Config.config import csv_files_path
from Config.config import txt_files_path
from ddt import ddt, file_data


#@ddt
class SgePoUnittest(unittest.TestCase):

    #@file_data("./Config/TestDataset/dataSet_ddt_po.json")
    def test_PurchaseOrder_Creacion_Nacional_SINDSO(self):

        #print("Test using: "+supplier)
        sge_funct = sge_functions()
        print("------------------------------Test to Create Purchase Order Nacional_SINDSO")

        sge_funct.sge_connection(login_data.username, login_data.ip, login_data.password)
        print("Trying to Connect...")
        print("Validating connection...")
        flag = sge_funct.validate_sge_connection()
        print(flag)
        if flag:
            lista_objetos = sge_funct.crear_lista_objetos(csv_files_path.csv_PurchaseOrder_Creacion_Nacional_SINDSO_TC)
            img_rclick = images.img_consulta_orden_de_compra
            img_doubleclick = images.img_inicio_orden_de_compra
            file_to_read =txt_files_path.txt_datos_productos_po
            sge_funct.create_general_po(lista_objetos, img_rclick, img_doubleclick, file_to_read, None, None)
            status_confirmada_por_proveedor = images.img_status_confirmada_por_proveedor
            print("Validating Purchase Order creation")
            if sge_funct.validating_po():
                #sge_funct.create_inv_txt_file()
                print("Validating Purchase confirmada por proveedor")
                if sge_funct.re_validate_status(status_confirmada_por_proveedor):
                    print("validado correctamente")
                    #sge_funct.create_inv_txt_file()
                else:
                    print("Fallo validado por proveedor")

        else:
            print(flag)
            assert flag



    def tearDown(self):
        sge_funct = sge_functions()
        sge_funct.terminate_sge_session()


if __name__ == '__main__':
    unittest.main()
