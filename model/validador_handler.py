from model.interface_handler import Handler

class ValidadorHandler(Handler):
    def handle(self, contexto):
        # 1. Valida Nome
        nome = contexto.get('nome_bruto')
        if not nome:
            contexto['erro'] = "O nome do atleta é obrigatório."
            return contexto

        # 2. Valida Números
        dados_strings = contexto.get('dados_brutos_strings', [])
        dados_convertidos = []
        
        if len(dados_strings) != 8:
            contexto['erro'] = "Faltam dados físicos."
            return contexto

        try:
            for valor_str in dados_strings:
                # Troca vírgula por ponto e converte
                valor_float = float(valor_str.replace(',', '.'))
                
                if valor_float <= 0:
                    contexto['erro'] = "Valores devem ser maiores que zero."
                    return contexto
                
                dados_convertidos.append(valor_float)

        except ValueError:
            contexto['erro'] = "Campos numéricos devem conter apenas números."
            return contexto

        # Salva dados limpos e segue
        contexto['dados_processados'] = dados_convertidos
        return super().handle(contexto)