import unittest
from Config.config import login_data, images, csv_files_path
from sge_functions.sge_functions import sge_functions
from Config.config import csv_files_path
from Config.config import txt_files_path
from ddt import ddt, file_data


#@ddt
class SgePoUnittest(unittest.TestCase):

    #@file_data("./Config/TestDataset/dataSet_ddt_po.json")
    def test_PurchaseOrder_Creacion_Nacional_Fact_Valida(self):
        """ ESTE TEST CASE ES UTIL PARA GENERAR FACTURAS CON STATUS  'EN TRANSITO' PARA OTROS TEST CASES"""
        #print("Test using: "+supplier)
        sge_funct = sge_functions()
        print("------------------------------Test to Create Purchase Order Nacional Factura Valida")

        #sge_funct.connection(login_data.linux_username, login_data.ip, login_data.password)
        print("Trying to establish SFTP Connection...")
        sge_funct.sftp_connection()
        print("Validating connection...")
        flag = sge_funct.validate_sftp_connection()
        print(flag)
        if flag:
            lista_objetos = sge_funct.crear_lista_objetos(csv_files_path.csv_PurchaseOrder_Asignacion_Factura_Nacional_Valida_TC)
            img_rclick = images.img_consulta_orden_de_compra
            img_doubleclick = images.img_inicio_orden_de_compra
            file_to_read = txt_files_path.txt_datos_productos_po
            sge_funct.create_general_po(lista_objetos, img_rclick, img_doubleclick, file_to_read, None, None)
            print(sge_funct.po_seleccionada)
            print("Validating Purchase Order Status")
            img_status = images.img_status_en_transito
            nombre_status = "EN TRANSITO"

            if sge_funct.validar_po_status(img_status, nombre_status):
                print("Validating Status 'En transito'")
                if sge_funct.re_validate_status(img_status):
                    print("validado correctamente")
                    sge_funct.mover_factura_status_en_trasito()
                else:
                    print("Fallo validacion, estatus Incorrecto")

        else:
            print(flag)
            assert flag


    def tearDown(self):
        sge_funct = sge_functions()
        sge_funct.terminate_sge_session()


if __name__ == '__main__':
    unittest.main()
