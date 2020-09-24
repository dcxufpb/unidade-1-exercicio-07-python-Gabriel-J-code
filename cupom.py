# coding: utf-8

def dados_loja_param(nome_loja, logradouro, numero, complemento, bairro, municipio, estado, cep, telefone, observacao, cnpj, inscricao_estadual):
	if not nome_loja:
		raise Exception("O campo nome da loja é obrigatório")
	
	if not logradouro:
		raise Exception("O campo logradouro do endereço é obrigatório")
		
	if not municipio:
		raise Exception("O campo município do endereço é obrigatório")

	if not estado:
		raise Exception("O campo estado do endereço é obrigatório")

	if not cnpj:
		raise Exception("O campo CNPJ da loja é obrigatório")	

	if not inscricao_estadual:
		raise Exception("O campo inscrição estadual da loja é obrigatório")

	_numero = "s/n" if not numero else str(numero)
	
	_complemento = " " + complemento if complemento else ""	

	_bairro = bairro + " - " if bairro else ""

	_cep = "CEP:" + cep if cep else ""
	
	_telefone = "Tel " + telefone if telefone else ""
	
	_telefone = " " + _telefone if cep and telefone else _telefone

	_observacao = observacao if observacao else ""

	nota = nome_loja + "\n"
	nota += "%s, %s%s\n" %(logradouro,_numero,_complemento)
	nota += "%s%s - %s\n" % (_bairro,municipio,estado)
	nota += "%s%s\n" % (_cep,_telefone)
	nota += "%s\n" % (_observacao)
	nota += "CNPJ: %s\n" %(cnpj)
	nota += "IE: %s" % (inscricao_estadual)

	return nota 
