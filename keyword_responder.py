class KeywordResponder:

    def get_response(self, preprocessed_text):
        has_instituicao = any(keyword in preprocessed_text for keyword in ["instituicao", "ifal", "campus"])
        has_contato = "contato" in preprocessed_text
        has_curso = any(keyword in preprocessed_text for keyword in ["curso", "cursos"])
        has_biblioteca = "biblioteca" in preprocessed_text
        
        def read_knowledge_file(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read().strip()

        # Verificar a correspondência com as palavras-chave
        if has_instituicao and any(keyword in preprocessed_text for keyword in ["endereco", "localizacao", "localizada", "localizado", "situada", "situado"]):
            response = "knowledge base\endereco.txt"
            return read_knowledge_file(response)
        
        elif has_instituicao and any(keyword in preprocessed_text for keyword in ["horario", "funcionamento", "hora", "turno"]):
            response = "knowledge base\funcionamento.txt"
            return read_knowledge_file(response)
        
        elif has_instituicao and any(keyword in preprocessed_text for keyword in ["chegar", "caminho", "mapa"]):
            response = "knowledge base\mapa.txt"
            return read_knowledge_file(response)
        
        elif has_contato and any(keyword in preprocessed_text for keyword in ["instituicao", "contato", "ifal", "campus", "secretaria", "suporte", "coordenacao", "atendimento", "atendido", "email"]):
            response = "knowledge base\contato.txt"
            return read_knowledge_file(response)
        
        elif has_curso and any(keyword in preprocessed_text for keyword in ["curso", "cursos", "oferecido", "ofertado", "disponível", "duracao", "tecnicos"]):
            response = "knowledge base\cursos.txt"
            return read_knowledge_file(response)
        
        elif any (keyword in preprocessed_text for keyword in ["site", "redes", "instagram", "facebook", "twitter", "instagram", "redes"]):
            response = "knowledge base\redessociais.txt"
            return read_knowledge_file(response)
      
        elif any (keyword in preprocessed_text for keyword in ["matricula", "documentacao", "documentos", "selecao", "admissao", "entrada"]):
            response = "knowledge base\matricula.txt"
            return read_knowledge_file(response)

        elif any (keyword in preprocessed_text for keyword in ["calendario", "feriados", "aula"]):
            response = "knowledge base\calendario.txt"
            return read_knowledge_file(response)

        elif any (keyword in preprocessed_text for keyword in ["bolsas", "bolsa", "intercambio"]):
            response = "knowledge base\bolsas.txt"
            return read_knowledge_file(response)

        elif any (keyword in preprocessed_text for keyword in ["editais", "oportunidades", "oportunidade"]):
            response = "knowledge base\editais.txt"
            return read_knowledge_file(response)

        elif any (keyword in preprocessed_text for keyword in ["laboratorio", "laboratorios"]):
            response = "knowledge base\laboratorios.txt"
            return read_knowledge_file(response)

        elif any (keyword in preprocessed_text for keyword in ["impressora", "xerox", "copia", "apostila"]):
            response = "knowledge base\impressoras.txt"
            return read_knowledge_file(response)

        elif has_biblioteca and any (keyword in preprocessed_text for keyword in ["funcionamento", "horario", "dias", "aberto", "aberta"]):
            response = "knowledge base\biblioteca.txt"
            return read_knowledge_file(response)

        elif any (keyword in preprocessed_text for keyword in ["livros", "livro", "emprestimo", "devolucao"]):
            response = "knowledge base\livros.txt"
            return read_knowledge_file(response)

        elif any (keyword in preprocessed_text for keyword in ["orientacao", "sobrecarregado", "necessidades", "apoio", "ajuda", "auxilio", "auxiliar", "dificil", "remedio", "medicamento"]):
            response = "knowledge base\canaisdeapoio.txt"
            return read_knowledge_file(response)

        elif any (keyword in preprocessed_text for keyword in ["assistencia", "vulnerabilidade", "vulneravel", "alimento", "alimentacao", "moradia","transporte"]):
            response = "knowledge base\assistencia.txt"
            return read_knowledge_file(response)

        elif any (keyword in preprocessed_text for keyword in ["inclusão", "deficiencia", "deficiente","capacitismo"]):
            response = "knowledge base\inclusao.txt"
            return read_knowledge_file(response)

        elif any (keyword in preprocessed_text for keyword in ["psicologa", "psicologico", "psicologo", "suicidio", "bullying", "medo", "tristeza", "emocionado", "emocional", "estranho", "triste", "matar", "cortar"]):
            response = "knowledge base\psicologo.txt"
            return read_knowledge_file(response)

        elif any (keyword in preprocessed_text for keyword in ["ouvidoria", "denuncia", "policia", "crime", "injustica", "reclamar", "reclamacao", "reclamacoes", "elogio", "elogios", "sugestao", "sugestoes", "manifestacao", "manifestacoes", "demanda"]):
            response = "knowledge base\ouvidoria.txt"
            return read_knowledge_file(response)

        elif any (keyword in preprocessed_text for keyword in ["eventos", "evento", "palestra", "esporte", "musica", "extensao", "workshop", "seminarios", "apresentacao", "feiras", "feira", "integracao"]):
            response = "knowledge base\eventos.txt"
            return read_knowledge_file(response)

        elif any (keyword in preprocessed_text for keyword in ["cantina", "refeitorio", "restaurante", "copa"]):
            response = "knowledge base\cantina.txt"
            return read_knowledge_file(response)

        elif any (keyword in preprocessed_text for keyword in ["estagio", "intercambio"]):
            response = "knowledge base\estagio.txt"
            return read_knowledge_file(response)

        elif any (keyword in preprocessed_text for keyword in ["politicas", "conduta", "faltas", "faltar", "faltei", "etica", "obediencia", "regimento", "moral", "avaliacao", "avaliacoes", "respeito", "infracao"]):
            response = "knowledge base\etica.txt"
            return read_knowledge_file(response)

        elif any (keyword in preprocessed_text for keyword in ["obrigado", "obrigada", "agradecido","agradecida"]):
            response = "knowledge base\agradecimento.txt"
            return read_knowledge_file(response)
        
        elif any (keyword in preprocessed_text for keyword in ["oi", "ola"]):
            response = "knowledge base\saudacao.txt"
            return read_knowledge_file(response)
        
        elif any (keyword in preprocessed_text for keyword in ["apenas isso", "tudo certo"]):
            response = "knowledge base\ok.txt"
            return read_knowledge_file(response)


        else:
            return "Desculpe, não entendi o que você está procurando. Por favor, reformule sua pergunta de forma mais descritiva.\n\nVocê está se referindo ao IFAL ou algum ambiente/atividade em específico?"
       