import telebot
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from unidecode import unidecode

nltk.download("punkt")
nltk.download("stopwords")

class TelegramBot:
    def __init__(self, token):
        self.TOKEN = token
        self.bot = telebot.TeleBot(self.TOKEN)
        self.stemmer = PorterStemmer()
        self.stop_words = set(stopwords.words("portuguese"))

        self.bot.message_handler(commands=['start', 'help'])(self.send_welcome)
        self.bot.message_handler(func=lambda message: True)(self.handle_message)

    def preprocess_text(self, text):
        text = text.lower()
        text = unidecode(text)
        text = ''.join(c for c in text if c.isalnum() or c.isspace())

        tokens = nltk.word_tokenize(text)
        tokens = [token for token in tokens if token not in self.stop_words]

        tokens = [self.stemmer.stem(token) for token in tokens]

        preprocessed_text = ' '.join(tokens)
        return preprocessed_text

    def send_welcome(self, message):
        welcome_msg = "Olá! Bem-vindo(a) ao chat de suporte do Instituto Federal de Alagoas (IFAL) Campus Arapiraca. \n\nVocê pode me perguntar sobre tudo relacionado a instituição! \n\n(como contatos, eventos, cursos, recursos, etc)\n\n Como posso ajudá-lo(a) hoje?"
        self.bot.reply_to(message, welcome_msg)

    def handle_message(self, message):
        preprocessed_text = self.preprocess_text(message.text)

        # Declaração das palavras-chave principais
        has_instituicao = any(keyword in preprocessed_text for keyword in ["instituicao", "ifal", "campus"])
        has_contato = "contato" in preprocessed_text
        has_curso = any(keyword in preprocessed_text for keyword in ["curso", "cursos"])
        has_biblioteca = "biblioteca" in preprocessed_text

        # Verificar a correspondência com as palavras-chave
        if has_instituicao and any(keyword in preprocessed_text for keyword in ["endereco", 
                                                                                "localizacao", 
                                                                                "localizada",
                                                                                "localizado", 
                                                                                "situada",
                                                                                "situado"]):
            response = "O Instituto Federal de Alagoas - Campus Arapiraca está localizado na Rodovia estadual AL-110, 359, bairro Deputado Nezinho, Arapiraca. Cep 57.317\n\nDigite a palavra MAPA para ter acesso ao Google Maps!"
        
        elif has_instituicao and any(keyword in preprocessed_text for keyword in ["horario", 
                                                                                "funcionamento", 
                                                                                "hora", 
                                                                                "turno"]):
            response = "O Instituto Federal de Alagoas - Campus Arapiraca funciona de segunda a sexta-feira, em horário comercial, ou seja, das 8h às 12h e das 13h às 17h."
        
        elif has_instituicao and any(keyword in preprocessed_text for keyword in ["chegar",
                                                                                "caminho",
                                                                                "mapa"]):
            response = "Para chegar até o Instituto Federal de Alagoas - Campus Arapiraca você pode seguir o endereço através do Google Maps: \n\nhttps://www.google.com/maps/place/Instituto+Federal+de+Alagoas,+Campus+Arapiraca/@-9.7454072,-36.6339326,17z/data=!3m1!4b1!4m6!3m5!1s0x705d5a26696e665:0x8c850bed9f271d22!8m2!3d-9.7454125!4d-36.6313577!16s%2Fg%2F11ckxwpg04?entry=ttu"
        
        elif has_contato and any(keyword in preprocessed_text for keyword in ["instituicao",
                                                                            "ifal",
                                                                            "campus",
                                                                            "secretaria",
                                                                            "suporte",
                                                                            "coordenacao",
                                                                            "atendimento",
                                                                            "atendido",
                                                                            "email"]):
            response = "Telefone IFAL Campus Arapiraca: \n\n+55 (82) 3522-1740\n\nAo falar com a equipe do IFAL, você poderá solicitar o contato específico da secretaria, suporte ao aluno ou coordenação que precisa para tratar de suas questões ou obter mais informações sobre os serviços oferecidos pela instituição."
        
        elif has_curso and any(keyword in preprocessed_text for keyword in ["curso",
                                                                            "cursos",
                                                                            "oferecido",
                                                                            "ofertado",
                                                                            "disponível",
                                                                            "area de atuacao",
                                                                            "duracao",
                                                                            "carga horaria",
                                                                            "tecnicos"]):
            response = "No Instituto Federal de Alagoas (IFAL) Campus Arapiraca, há os seguintes cursos:\n\n1. Técnico em Informática: Carga horária em torno de 1.200 horas e duração de 2 anos. Área de atuação: Desenvolvimento e suporte de sistemas, manutenção de hardware e redes, entre outros.\n\n2. Técnico em Eletrotécnica: Carga horária em torno de 1.200 horas e duração de 2 anos. Área de atuação: Instalação e manutenção de sistemas elétricos, automação, controle de processos industriais, entre outros.\n\n3. Técnico em Química: Carga horária em torno de 1.200 horas e duração de 2 anos. Área de atuação: Análises laboratoriais, controle de qualidade, produção industrial, entre outros.\n\nPara mais informações, acesso o site da instituição: \nhttp://www2.ifal.edu.br/"

        elif any (keyword in preprocessed_text for keyword in ["site",
                                                            "redes",
                                                            "seguir",
                                                            "instagram",
                                                            "facebook",
                                                            "twitter",
                                                            "instagram",
                                                            "redes sociais"]):
            response = "Para encontrar o IFAL Campus Arapiraca na internet, basta acessar:\n\nSite oficial do IFAL: http://www2.ifal.edu.br/ \n\nE nas Redes Sociais:\n\nInstagram do IFAL: @ifaloficial\n\nTwitter do IFAL: @ifal_oficial"

        elif any (keyword in preprocessed_text for keyword in ["matricula",
                                                            "documentacao",
                                                            "inscricao",
                                                            "documentos",
                                                            "prazos",
                                                            "o que levar"]):
            response = "Para realizar sua matrícula no IFAL, os documentos exígidos são os seguintes:\n\n1. Documento de Identidade (RG) e CPF (do aluno e do responsável, se menor de idade).\n\n2. Certidão de Nascimento ou Casamento.\n\n3. Comprovante de residência.\n\n4. Foto 3x4 recente.\n\n5. Certificado de Reservista (para candidatos do sexo masculino maiores de 18 anos).\n\nO IFAL costuma divulgar as informações sobre a documentação necessária e os prazos de matrícula no edital do processo seletivo ou em seu site oficial, acesse para saber mais: \n\nhttp://www2.ifal.edu.br/"

        elif any (keyword in preprocessed_text for keyword in ["calendario",
                                                            "feriados",
                                                            "aula"]):
            response = "Tenha acesso a todo o planejamento do ano letivo no Instituto Federal de Alagoas (IFAL) Campus Arapiraca acessando seu calendário acadêmico presente na seguinte página web:\n\nhttps://www2.ifal.edu.br/campus/arapiraca/ensino/calendario-academico"

        elif any (keyword in preprocessed_text for keyword in ["bolsas",
                                                            "bolsa",
                                                            "intercambio",
                                                            "mobilidade academica"]):
            response = "No presente, o IFAL disponibiliza bolsas de estudo para alunos com dificuldades financeiras, que podem ser integrais ou parciais, dependendo das circunstâncias do aluno.\n\n Além disso, a instituição oferece oportunidades de intercâmbio para estudantes que desejam aprimorar seus conhecimentos em outros países, participando de experiências educacionais em instituições estrangeiras parceiras.\n\n O IFAL também possui programas de mobilidade acadêmica, permitindo que os alunos estudem temporariamente em outros campi do instituto ou em instituições parceiras dentro do Brasil, enriquecendo suas experiências acadêmicas e culturais."

        elif any (keyword in preprocessed_text for keyword in ["editais",
                                                            "oportunidades",
                                                            "oportunidade"]):
            response = "Tenha acesso as chamadas de novas oportunidades para estudantes do IFAL através do link: \n\nhttps://www2.ifal.edu.br/o-ifal/ensino/editais"

        elif any (keyword in preprocessed_text for keyword in ["laboratorio",
                                                            "laboratorios"]):
            response = "No presente, o IFAL Campus Arapiraca conta com laboratórios de informática para atender às necessidades dos cursos e alunos da área de Tecnologia da Informação e afins. Esses laboratórios são equipados com computadores, acesso à internet e software específico para o ensino de disciplinas relacionadas à informática, programação, design, entre outras áreas."

        elif any (keyword in preprocessed_text for keyword in ["impressora",
                                                            "xerox",
                                                            "copia",
                                                            "apostila"]):
            response = "Atualmente, o IFAL Campus Arapiraca conta com dois locais de impressão disponíveis para seus alunos e membros da comunidade acadêmica. Esses locais são: biblioteca e laboratório de informática 001. \n\nOs alunos podem acessar impressoras para imprimir materiais acadêmicos, trabalhos e outros documentos relacionados aos estudos. As políticas de uso, como quantidade de páginas permitidas e custos associados, variam de acordo com as normas atuais da administração das máquinas de impressão."

        elif has_biblioteca and any (keyword in preprocessed_text for keyword in ["biblioteca",
                                                                                "funcionamento",
                                                                                "horario",
                                                                                "dias",
                                                                                "aberto",
                                                                                "aberta"]):
            response = "No presente, a biblioteca do IFAL Campus Arapiraca funciona como um recurso essencial para alunos, professores e funcionários, oferecendo um acervo de livros, periódicos e outros materiais educacionais para apoio às atividades acadêmicas.\n\nNo geral, as bibliotecas do IFAL costumam operar durante o horário comercial, de segunda a sexta-feira, com uma pausa no horário de almoço.\n\nPara saber sobre empréstimo e devolução de livros digite: \n\nLIVROS"

        elif any (keyword in preprocessed_text for keyword in ["livros",
                                                            "livro",
                                                            "emprestimo",
                                                            "devolucao"]):
            response = "O procedimento de empréstimo e devolução de livros na biblioteca segue um sistema organizado. \n\nAlunos e membros da comunidade acadêmica precisam se cadastrar e obter uma carteirinha de identificação para realizar empréstimos. O cadastro é feito na própria biblioteca possuindo sistema de biometria. \n\nO número de livros permitidos e o prazo de devolução variam de acordo com políticas internas vigentes no momento na instituição, mas geralmente é possível pegar um total de 4 livros desde que não sejam da mesma edição, com um prazo de devolução de até 14 dias."

        elif any (keyword in preprocessed_text for keyword in ["orientacao",
                                                            "sobrecarregado",
                                                            "necessidades",
                                                            "canais de apoio",
                                                            "apoio",
                                                            "ajuda",
                                                            "auxilio",
                                                            "auxiliar",
                                                            "dificil",
                                                            "preciso",
                                                            "remedio",
                                                            "medicamento"]):
            response = "O IFAL oferece diversos canais de apoio ao estudante para auxiliar em suas necessidades acadêmicas e pessoais. Alguns dos principais canais de apoio são:\n\n1. Coordenação de Curso: Cada curso possui uma coordenação acadêmica que pode fornecer orientações sobre o currículo, disciplinas e questões relacionadas ao curso em si.\n> Para saber mais escreva CONTATO COORDENAÇÃO\n\n2. Setor de Assistência Estudantil: Esse setor é responsável por oferecer apoio aos estudantes em situação de vulnerabilidade socioeconômica, disponibilizando bolsas, auxílio alimentação, moradia, transporte e outros benefícios.\n> Para saber mais digite ASSISTÊNCIA\n\n3. Núcleo de Atendimento às Pessoas com Necessidades Específicas (NAPNE): Esse núcleo é responsável por prestar assistência e promover a inclusão de estudantes com deficiência ou necessidades educacionais especiais.\n> Para saber mais digite INCLUSÃO\n\n4. Núcleo de Apoio Psicopedagógico (NAP): O NAP oferece serviços de orientação psicológica e pedagógica, auxiliando os estudantes em questões emocionais e acadêmicas.\n> Para saber mais digite PSICOLOGICO\n\n5. Ouvidoria: A Ouvidoria é um canal de comunicação para receber reclamações, sugestões e elogios dos estudantes, proporcionando um espaço para expressar suas opiniões.\n> Para saber mais digite OUVIDORIA\n\n6. Professores e Tutores: Os próprios docentes e tutores dos cursos também estão disponíveis para fornecer orientações e esclarecer dúvidas acadêmicas.\n\nEsses são alguns dos principais canais de apoio ao estudante no IFAL."

        elif any (keyword in preprocessed_text for keyword in ["assistencia",
                                                            "vulnerabilidade",
                                                            "vulneravel",
                                                            "alimento",
                                                            "alimentacao",
                                                            "moradia",
                                                            "transporte"]):
            response = "O Setor de Assistência Estudantil é uma importante área de suporte oferecida pelo Instituto Federal de Alagoas (IFAL) para auxiliar os estudantes em suas necessidades socioeconômicas. O principal objetivo desse setor é promover a inclusão e garantir igualdade de oportunidades para os alunos, especialmente aqueles em situação de vulnerabilidade financeira.\n\nAbaixo estão listadas as principais assistências disponíveis:\n\n1. Bolsas de estudo: São concedidas bolsas integrais ou parciais para alunos que comprovem carência financeira, permitindo que continuem seus estudos sem dificuldades financeiras.\n\n2. Auxílio Alimentação: O IFAL oferece auxílio financeiro para ajudar os estudantes a custear suas refeições enquanto estão na instituição\n\n3. Moradia Estudantil: Alguns campi do IFAL oferecem moradia estudantil para alunos que residem em outras cidades ou regiões, proporcionando uma opção de alojamento durante o período de estudos.\n\n4. Auxílio Transporte: O setor também pode disponibilizar auxílio financeiro para o transporte dos alunos, facilitando o acesso ao campus e aos locais de estágio ou prática profissional.\n\nPara ter acesso a essas assistências acesse o site da instituição e fique de olho nos editais.\n\nOBS: para casos mais urgentes contacte-nos através do número: +55 (82) 3522-1780"

        elif any (keyword in preprocessed_text for keyword in ["inclusão",
                                                            "deficiencia",
                                                            "deficiente",
                                                            "capacitismo"]):
            response = "O Núcleo de Atendimento às Pessoas com Necessidades Específicas (NAPNE) é o núcleo responsável por prestar assistência e promover a inclusão de estudantes com deficiência ou necessidades educacionais especiais.\n\nPara entrar em contato com o NAPNE ou saber mais sobre como são realizadas suas funções, entre em contato através do email apoionapne@ifal.com.br"

        elif any (keyword in preprocessed_text for keyword in ["psicologa",
                                                            "psicologico",
                                                            "psicologo",
                                                            "suicidio",
                                                            "bullying",
                                                            "medo",
                                                            "tristeza",
                                                            "emocionado",
                                                            "emocional",
                                                            "estranho",
                                                            "pensamentos ruins",
                                                            "pensamentos maus",
                                                            "triste",
                                                            "matar",
                                                            "cortar"]):
            response = "VOCÊ NÃO ESTÁ SÓ!\n\nO NAP oferece serviços de orientação psicológica e pedagógica, auxiliando os estudantes em questões emocionais e acadêmicas.\n\nEntre em contato conosco através do telefone +55 (82) 3522-1750 ou nos procure presencialmente no NAP IFAL Sala 09 corredor 01"

        elif any (keyword in preprocessed_text for keyword in ["ouvidoria",
                                                            "denuncia",
                                                            "policia",
                                                            "crime",
                                                            "injustica",
                                                            "reclamar",
                                                            "reclamacao",
                                                            "reclamacoes",
                                                            "elogio",
                                                            "elogios",
                                                            "sugestao",
                                                            "sugestoes",
                                                            "manifestacao",
                                                            "manifestacoes",
                                                            "demanda"]):
            response = "A Ouvidoria é um canal de comunicação institucional que atua como intermediária entre os membros da comunidade acadêmica (alunos, professores, servidores e demais interessados) e a administração do Instituto Federal de Alagoas (IFAL). O principal objetivo da Ouvidoria é garantir um espaço de diálogo, transparência e resolução de demandas, ouvindo as manifestações, reclamações, sugestões e elogios dos usuários da instituição.\n\nAs atribuições da Ouvidoria incluem:\n\n1. Receber e analisar manifestações: A Ouvidoria recebe e registra as manifestações dos usuários relacionadas a diversos assuntos, como problemas administrativos, questões acadêmicas, serviços, infraestrutura, entre outros.\n\n2. Encaminhar demandas: Após a análise, a Ouvidoria encaminha as demandas recebidas para os setores competentes, a fim de que sejam devidamente apuradas e respondidas.\n\n3. Acompanhamento e resposta: A Ouvidoria acompanha o andamento das demandas encaminhadas, assegurando que as respostas sejam providenciadas de forma adequada e dentro dos prazos estabelecidos.\n\n4. Manter a confidencialidade e a imparcialidade: A Ouvidoria trata as manifestações com sigilo e imparcialidade, garantindo que as informações sejam tratadas de forma ética e respeitosa.\n\n5. Proporcionar melhorias: Além de solucionar problemas individuais, a Ouvidoria também pode identificar padrões de ocorrências e propor melhorias nos processos e serviços da instituição.\n\nA Ouvidoria é um importante instrumento de participação e cidadania, que possibilita aos membros da comunidade acadêmica exercerem seus direitos e contribuírem para o aprimoramento contínuo do IFAL. Os contatos com a Ouvidoria podem ser realizados de forma presencial, por telefone, por e-mail ou por meio de formulários online, conforme disponibilizado pelo IFAL em seu site oficial.\n\nÉ essencial ressaltar que a Ouvidoria é independente e autônoma, e suas ações são norteadas por princípios éticos e transparentes, visando a promover um ambiente institucional cada vez mais democrático e responsável."

        elif any (keyword in preprocessed_text for keyword in ["eventos",
                                                            "evento",
                                                            "palestra"
                                                            "esporte",
                                                            "musica",
                                                            "extensao",
                                                            "workshop",
                                                            "seminarios",
                                                            "apresentacao",
                                                            "feiras",
                                                            "feira",
                                                            "integracao",
                                                            "semanas academicas"]):
            response = "O IFAL (Instituto Federal de Alagoas) realiza diversos eventos ao longo do ano, proporcionando aos alunos, docentes e à comunidade em geral oportunidades de aprendizado, interação e integração. Esses eventos podem ser acadêmicos, culturais, esportivos e de extensão, enriquecendo a experiência educacional dos estudantes e estimulando a troca de conhecimento e experiências.\n\nOs eventos mais comuns são:\n\n1. Semanas Acadêmicas: São eventos específicos de cada curso ou área do conhecimento.\n\n2. Feiras de Ciências e Tecnologia: Eventos que promovem a divulgação e exposição de projetos desenvolvidos pelos alunos nas áreas de ciências e tecnologia.\n\n 3. Torneios Esportivos: Competições esportivas envolvendo diferentes modalidades esportivas.\n\n4. Ações de Extensão: Eventos que envolvem a comunidade externa ao IFAL, proporcionando serviços, cursos e ações de cunho social e educacional.\n\nPara saber sobre eventos atuais visite nossas Redes Sociais: \n\nInstagram do IFAL: @ifaloficial\n\nTwitter do IFAL: @ifal_oficial"

        elif any (keyword in preprocessed_text for keyword in ["cantina",
                                                            "refeitorio",
                                                            "restaurante",
                                                            "copa"]):
            response = "Geralmente os campi do IFAL contam com espaços como copa, cantina e/ou restaurante para atender as necessidades dos alunos e membros da comunidade acadêmica"

        elif any (keyword in preprocessed_text for keyword in ["estagio",
                                                            "intercambio"]):
            response = "Para saber informações detalhadas sobre estágio ou intercâmbio via IFAL, consulte os editais disponíveis através do site:\n\nhttps://www2.ifal.edu.br/campus/arapiraca/editais"

        elif any (keyword in preprocessed_text for keyword in ["politicas",
                                                            "conduta",
                                                            "faltas",
                                                            "faltar",
                                                            "faltei",
                                                            "etica",
                                                            "obediencia",
                                                            "regimento",
                                                            "moral",
                                                            "avaliacao",
                                                            "avaliacoes",
                                                            "respeito",
                                                            "infracao"]):
            response = "As regras e políticas relacionadas a faltas, avaliações e ética acadêmica são fundamentais para o bom funcionamento e a qualidade do ensino em instituições como o Instituto Federal de Alagoas (IFAL). Essas normas visam garantir a regularidade e a integridade do processo educacional, bem como o respeito aos princípios éticos e de responsabilidade no ambiente acadêmico.\n\nFALTAS\n\nO IFAL geralmente possui normas sobre frequência e controle de faltas dos alunos. As faltas excessivas podem acarretar em sanções, como a impossibilidade de realizar provas ou de ser aprovado em uma disciplina. É importante que os alunos estejam atentos ao limite de faltas permitido em cada disciplina e às consequências estabelecidas em caso de ultrapassagem desse limite.\n\nAVALIAÇÕES:\n\nAs avaliações são uma parte essencial do processo de aprendizagem e são utilizadas para medir o desempenho acadêmico dos alunos. O IFAL geralmente possui regulamentações específicas sobre o formato, conteúdo e critérios de avaliação de cada disciplina. É fundamental que os alunos estejam cientes das datas das provas e que se preparem adequadamente para elas.\n\nÉTICA ACADÊMICA:\n\nA ética acadêmica é uma questão central em instituições de ensino e representa o compromisso com a honestidade, integridade e respeito às normas estabelecidas. Plágio, fraude em provas, cópia de trabalhos sem atribuição de autoria e outras práticas antiéticas são consideradas infrações graves e podem resultar em punições, como notas reduzidas, reprovação ou até mesmo medidas disciplinares mais severas."

        elif any (keyword in preprocessed_text for keyword in ["obrigado",
                                                               "obrigada",
                                                               "agradecido",
                                                               "agradecida"]):
            response = "Estou a sua disposição!\n\nDigite OK para finalizar a conversa"

        else:
            response = "Desculpe, não entendi o que você está procurando. Por favor, reformule sua pergunta de forma mais descritiva."
        
        self.bot.reply_to(message, response)


    def start_polling(self):
        self.bot.polling()
