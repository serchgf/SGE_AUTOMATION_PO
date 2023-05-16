import unittest
from Config.config import login_data, images, csv_files_path
from sge_functions.sge_functions import sge_functions
from Config.config import csv_files_path
from Config.config import txt_files_path
from ddt import ddt, file_data


#@ddt
class SgePoUnittest(unittest.TestCase):

    #@file_data("./Config/TestDataset/dataSet_ddt_po.json")
    def test_PurchaseOrder_AsignacionFactura_Nacional_Cancelacion(self):

        #print("Test using: "+supplier)
        sge_funct = sge_functions()
        print("------------------------------Test to Create Purchase Order Asignacion Factura Nacional cancelacion")

        #sge_funct.connection(login_data.linux_username, login_data.ip, login_data.password)
        print("Trying to establish SFTP Connection...")
        sge_funct.sftp_connection()
        print("Validating connection...")
        flag = sge_funct.validate_sftp_connection()
        print(flag)


        if flag:
            lista_objetos = sge_funct.crear_lista_objetos(csv_files_path.csv_PurchaseOrder_Asignacion_Factura_Nacional_Cancelacion_TC)
            img_rclick = images.img_rclick_buscar_factura_tc4
            img_doubleclick = images.img_inicio_orden_de_compra

            archivo_productos = txt_files_path.txt_datos_productos_po
            fact_valida = txt_files_path.fact_valida_txt_file
            fact_invalida = txt_files_path.fact_invalida_txt_file
            sge_funct.create_general_po(lista_objetos, img_rclick, None, None, None, fact_invalida)
            print(sge_funct.po_seleccionada)
            # print("Validating Purchase Order Status...")
            # img_status = images.img_status_en_transito
            # if sge_funct.validar_po_status(img_status):
            #     #sge_funct.create_inv_txt_file()
            #     print("Status 'Cancelacion' validado correctamente")
            #     if sge_funct.validar_status_post_job(img_status):
            #         print("validado correctamente")
            #         #sge_funct.create_inv_txt_file()
            #     else:
            #         print("Fallo validacion, estatus Incorrecto")
            # else:
            #     print("Fallo validacion, estatus Incorrecto")


        else:
            print(flag)
            assert flag


    def tearDown(self):
        sge_funct = sge_functions()
        #sge_funct.terminate_sge_session()


if __name__ == '__main__':
    unittest.main()
