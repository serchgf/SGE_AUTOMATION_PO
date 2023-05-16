"""
pip install pytest-html
install pip install ansi2html
pip install ddt
"""
import os


class login_data:
    # uat02
    ambiente = "UAT02"
    programas = "verxx"
    username = "itmx12"
    password = "sgem5986"
    ip = "192.168.1.3"
    usuario_de_compras = "sfabian"

    adm_username ='itmx16'
    adm_password = "sgeg4913"
    usuario_adm_grecia = "grejudl"

class data_sftp_connection:
    sftp_hostname = "192.168.1.3"
    sftp_username = "itmx12"
    sftp_password = "sgem5986"
    sftp_port = "22"

class csv_files_path:
    main_dir = "Config/TestDataSet/"
    csv_PurchaseOrder_Creacion_Nacional_DSO_TC = "Config/TestDataSet/PurchaseOrder_Creacion_Nacional_DSO_TC.csv"
    csv_PurchaseOrder_Creacion_Nacional_SINDSO_TC = "Config/TestDataSet/PurchaseOrder_Creacion_Nacional_SINDSO_TC.csv"
    csv_PurchaseOrder_Asignacion_Factura_Nacional_Valida_TC = "Config/TestDataSet/PurchaseOrder_AsignacionFactura_Nacional_Valida_TC.csv"
    csv_PurchaseOrder_Asignacion_Factura_Nacional_Revision_TC = "Config/TestDataSet/PurchaseOrder_AsignacionFactura_Nacional_Revision_TC.csv"
    csv_PurchaseOrder_Asignacion_Factura_Nacional_Cancelacion_TC = "Config/TestDataSet/PurchaseOrder_AsignacionFactura_Nacional_Cancelacion_TC.csv"
    csv_datos_productos_po = "Config/TestDataSet/datos_productos_po.csv"

class txt_files_path:
    main_dir = "Config/TestDataSet/"
    file_name = "tmpmasivo.txt"
    txt_file = main_dir + file_name
    txt_datos_productos_po = "Config/TestDataSet/datos_productos_po.txt"
    fact_invalida_txt_file = "Config/TestDataSet/Factura Invalida.txt"
    fact_valida_txt_file = "Config/TestDataSet/INV-012M0021200190RD.txt"
    txt_datos_productos_po_internacional = "Config/TestDataSet/datos_productos_po_internacional.txt"
    txt_psc_po_por_confirmar_internacional = "Config/TestDataSet/PSC-012A002120032236-10052023-172258.txt"
    fact_internacional_valida_txt = "Config/TestDataSet/INV-012A0021200336RD.txt"
    fact_internacional_invalida_txt = "Config/TestDataSet/INV-012A0021200336RDINV.txt"
    archivo_psc_base = "Config/TestDataSet/PSC-num_po-10052023-172258.txt"
    archivo_psc_base_name = "PSC-num_po-10052023-172258.txt"

    Confirmada_03_txt = "Config/TestDataSet/Cambios de Estatus (PSC)/Confirmada 03/PSC-012A002120032236-10052023-172258.txt"
    En_proceso_de_Cruce_14_txt = "Config/TestDataSet/Cambios de Estatus (PSC)/En proceso de Cruce 14/PSC-2159-962-181-110523-115017.txt"
    En_transito_nacional_16_txt = "Config/TestDataSet/Cambios de Estatus (PSC)/En Transito nacional 16/PSC-2159-962-181-110523-141855.txt"
    Pedimento_Pagado_13_txt = "Config/TestDataSet/Cambios de Estatus (PSC)/Pedimento Pagado 13/PSC-2159-962-181-110523-112206.txt"
    Recibida_11_txt = "Config/TestDataSet/Cambios de Estatus (PSC)/Recibida 11/PSC-012A002120032236-1-11052023-101020.txt"
    Revisada_Origen_10_txt = "Config/TestDataSet/Cambios de Estatus (PSC)/Revisada Origen 10/PSC-012A002120032236-110523-094521.txt"
    Revisada_12_txt = "Config/TestDataSet/Cambios de Estatus (PSC)/Revisada 12/PSC-012A002120032236-110523-102321.txt"


class files:
    directory_tmp_file = "tmp_file/"
    # --------------------------------------------------------------------........................ NACIONALES
    #inv_base_txt_file = "Config/TestDataSet/INV-Factura Invalida.txt"
    valid_inv_confirmed_po_file = "valid_inv_confirmed_po/"
    processed_inv_file = "processed_inv_file/"
    invalid_inv_folder = "invalid_inv_folder/"
    inv_confirmadas_validas_folder = "facturas_generadas/confirmadas_validas/"
    inv_canceladas_folder = "facturas_generadas/canceladas/"
    inv_en_transito_folder = "facturas_generadas/en_transito/"
    inv_invalidas_folder = "facturas_generadas/invalidas/"
    inv_procesadas_folder = "facturas_generadas/procesadas/"
    inv_recibida_en_revision_folder = "facturas_generadas/recibida_en_revision/"
    inv_recibida_parcial_y_se_espera_complemento_folder = "facturas_generadas/recibida_parcial_y_se_espera_complemento/"
    inv_recibido_total_folder = "facturas_generadas/recibido_total/"
    inv_en_proceso_de_acomodo_folder = "facturas_generadas/en_proceso_de_acomodo/"
    inv_acomodado_pendiente_de_entrada_folder = "facturas_generadas/acomodado_pendiente_de_entrada/"

    # --------------------------------------------------------------------........................ INTERNACIONALES
    internacionales_por_confirmar_03_SINDSO_folder = "facturas_internacionales/por_confirmar_03_SINDSO/"
    internacionales_por_confirmar_03_DSO_folder = "facturas_internacionales/por_confirmar_03_DSO/"
    internacionales_confirmada_03_DSO_folder = "facturas_internacionales/confirmada_03_DSO/"
    internacionales_confirmada_03_SINDSO_folder = "facturas_internacionales/confirmada_03_SINDSO/"
    internacionales_inv_valida_folder = "facturas_internacionales/inv_valida/"
    internacionales_inv_invalida_folder = "facturas_internacionales/inv_invalida/"
    internacionales_en_transito_folder = "facturas_internacionales/en_transito/"
    internacionales_cancelada_folder = "facturas_internacionales/cancelada/"
    internacionales_revisada_en_origen_10_folder = "facturas_internacionales/revisada_en_origen_10/"
    internacionales_recibida_11_folder = "facturas_internacionales/recibida_11/"
    internacionales_revisada_12_folder = "facturas_internacionales/revisada_12/"
    internacionales_pedimento_pagado_13_folder = "facturas_internacionales/pedimento_pagado_13/"
    internacionales_en_proceso_de_cruce_14_folder = "facturas_internacionales/en_proceso_de_cruce_14"
    internacionales_cruzada_15_folder = "facturas_internacionales/cruzada_15"
    internacionales_en_transito_nacional_16 = "facturas_internacionales/en_transito_nacional_16"
    internacionales_recibida_en_revision_20 = "facturas_internacionales/recibida_en_revision_20"
    internacionales_psc_status_10_folder = "facturas_internacionales/PSC_status_10/"
    internacionales_MUP_folder = "facturas_internacionales/MUP"
    internacionales_tmp_psc_folder = "facturas_internacionales/tmp_psc/"

    base_Confirmada_03_folder = "/Config/TestDataSet/Cambios de Estatus (PSC)/Confirmada 03/"
    base_En_proceso_de_Cruce_14_folder = "Config/TestDataSet/Cambios de Estatus (PSC)/En proceso de Cruce 14/"
    base_En_transito_nacional_16_folder = "Config/TestDataSet/Cambios de Estatus (PSC)/En Transito nacional 16/"
    base_Pedimento_Pagado_13_folder = "Config/TestDataSet/Cambios de Estatus (PSC)/Pedimento Pagado 13/"
    base_Recibida_11_folder = "Config/TestDataSet/Cambios de Estatus (PSC)/Recibida 11/"
    base_Revisada_Origen_10_folder = "Config/TestDataSet/Cambios de Estatus (PSC)/Revisada Origen 10/"
    base_Revisada_12_folder = "Config/TestDataSet/Cambios de Estatus (PSC)/Revisada 12/"


class images:
    """images location"""

    ROOT = os.path.abspath(os.path.join(".", os.pardir))
    img_sge_adm_pantalla_inicial = f"image_files/sge_adm_pantalla_inicial.png"
    img_pantalla_inicial = f"image_files/pantallaInicial.png"
    img_error_connection = f"image_files/errorConexion2.png"
    img_error_atraso_importante = f"image_files/Error atraso importante.png"
    img_error_gdl = f"image_files/error Guadalajara.png"
    img_invoice_created_correctly = f"image_files/folioGeneradoValidacion.png"
    img_rclick_carga_masiva = f"image_files/rclick_carga_masiva.png"
    img_rclick_buscar_factura_tc4 = f"image_files/rclick_buscar_factura_tc4.png"
    img_promociones = f"image_files/promociones.png"
    img_promociones2 = f"image_files/promociones2.png"
    img_inicio_orden_de_compra = "image_files/inicioOrdenCompra.png"
    img_consulta_orden_de_compra = "image_files/consulta_oc.png"
    img_confirmacion_colocada = "image_files/confirmacionColocada.png"
    img_status_confirmada_por_proveedor = "image_files/status_confirmada.png"
    img_header_orden_de_compra = "image_files/header_orden_de_compra.png"
    img_sftp_connection_valid = "image_files/sftp_connection_valid.png"
    img_status_job_ok = "image_files/status_job_ok.png"
    img_status_job_pend = "image_files/status_job_pend.png"
    img_suc_xx = "image_files/img_suc_xx.png"
    img_status_en_transito = "image_files/status_en_transito.png"
    img_status_recibida_en_proceso_de_revision = "image_files/status_recibida_en_proceso_de_revision.png"
    img_status_en_proceso_de_acomodo = "image_files/status_en_proceso_de_acomodo2.png"
    img_status_acomodada_pend_ent = "image_files/status_acomodada_pend_ent.png"
    img_status_cancelada_compras = "image_files/status_cancelada_compras.png"
    img_status_recibida_total = "image_files/status_recibida_total.png"
    img_status_revisada_en_origen = "image_files/status_revisada_en_origen.png"
    img_status_recibida_por_agte_ad = "image_files/status_recibida_por_agte_ad.png"
    img_status_revisada_por_agte_ad = "image_files/status_revisada_por_agte_ad.png"
    img_status_pedimento_pagado = "image_files/status_pedimento_pagado.png"

    #------------------------------INTERNACIONAL JOB SCP
    img_status_job_psc_internacional_ok = "image_files/status_job_psc_internacional_ok.png"


class commons_cmds:
    ctrle = "ctrl+e"
    ctrlo = "ctrl+o"
    ctrlw = "ctrl+w"
    ctrlk = "ctrl+k"
    ctrla = "ctrl+a"
    ctrlb = "ctrl+b"
    ctrlr = "ctrl+r"
    rclick = 'rclick'
    arrow_down = 'down'
    tab = "tab"
    doubleClick = 'doubleclick'
    bk_space = 'backspace'
    space = 'space'
    tiempo_fuera_2 = '2 segundos'
    tiempo_fuera_3 = '3 segundos'
    tiempo_fuera_5 = '5 segundos'
    tiempo_fuera_10 = '10 segundos'
    tiempo_fuera_20 = '20 segundos'
    promociones = 'promociones'
    leer_archivo = 'leer_archivo'
    subir_archivo = "subir_archivo"
    enter = 'Enter'
    validar_cdi = "validar_cdi"
    validar_job_ok = "validar_job_ok"
    validar_job_pend = "validar_job_pend"
    login_sge = "login_sge"
    login_adm_sge = "login_adm_sge"
    login_sftp = "login_sftp"
    pegar_num_inv_po = "pegar_num_inv_po"
    pegar_num_po = "pegar_num_po"
    subir_fact_invalida = "subir_factura_invalida"


class image_root:
    ROOT = os.path.abspath(os.path.join(".", os.pardir))
