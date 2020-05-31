import paciente as p
import medico as m 
import atendente as a

while True:
    pc = p.paciente()
    md = m.medico()
    at = a.atendente()

    menu1 = int(input("[1] Paciente\n[2] Medico\n[3] Atendente\n[4] Sair\n"))

    #Paciente
    if menu1 == 1:
        print("\nCADASTRO\n==============================")
        pc.cadastrar_paciente()
        print("\nEXIBIR\n==============================")
        pc.exibir_paciente()
        print("\n")

    #Médico
    elif menu1 == 2:
        print("\nCADASTRO\n==============================")
        md.cadastrar_medico()
        print("\nEXIBIR\n==============================")
        md.exibir_medico()
        print("\n")

    #Atendente
    elif menu1 == 3:
        print("\nCADASTRO\n==============================")
        at.cadastrar_atendente()
        print("\nEXIBIR\n==============================")
        at.exibir_atendente()
        print("\n")


    #Sair
    else:
        break