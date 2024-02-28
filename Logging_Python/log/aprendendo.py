import logging
import sys

from pythonjsonlogger import jsonlogger

"""
- Niveis de log
. Notset (0)
Menor nivel
Vai ser utilizado caso o nivel nao seja definido

. Debug (10)
Mensagens para debugar
Dao informacoes detalhadas sobre o comportamento de um codigo
Sao tipicamente usadas durante o desenvolvimento

. Info (20)
Sao usadas para logar as mensagens informacionais de um codigo
Essas mensagens podem ser usadas para acompanhar o progresso de
um programa ou para dar contexto ao usuario

. Warning (30)
Eh usado para logar mensagens que indicam potenciais erros ou
comportamentos inesperados no programa
Nao significam necessariamente um erro, mas sao uteis para diagnosticar
problemas

. Error (40)
Eh usado para logar mensagens que indicam que um erro ocorreu no
programa

. Critical (50)
Eh usado para indicar que um erro critico ocorreu e nao deixa
o programa funcionar corretamente
Essas mensagens so devem ser usadas quando necessario

- Logger
. Quando um logger eh criado, seu logging level eh setado como NOTSET
. NAO USAR O LEVEL NOTSET!

- Formato de uma linha no log
<LOG_LEVEL>:<logger_name>:<message>

- Root logger
. Warning level para cima
. Para loggar levels abaixo, tenho que setar o level no setup

- Logging Confing
. Uma das coisas que eu posso configurar eh quais mensagens
eu quero exibir no log (assim, eu posso controlar o volume de logs
gerado pela minha aplicacao)

- Eu posso criar novos niveis de log, mas primeiro quero usar o basico
"""
# Basic Setup
# Esse logger eh o root logger
logging.basicConfig()

"""
- Da para criar loggers customizados caso eu queira separar os logs
de diferentes partes do projeto em diferentes logs

- Para customizar o formato da saida e o comportamento de um logger
customizado:
. Handler
Especifica onde a mensagem deve ser enviada (console, file, http endpoit)

. Formatter
Responsavel por formatar a saida do log

. Filter
Decide se uma mensagem deve ser logada ou nao
"""


class RecordFilter(logging.Filter):
    def filter(self, record):
        return record.msg.startswith("Important:")


logger = logging.getLogger("aprendendo")
handler = logging.FileHandler("aprendendo.log")
# O FileHandler cria o arquivo, caso nao exista. Se existir,
# o FileHanlder abre o arquivo no modo append

string_format = "%(asctime)s | %(levelname)s | %(name)s : %(message)s"
formatter = logging.Formatter(string_format)

handler.setFormatter(formatter)
handler.addFilter(RecordFilter())

logger.addHandler(handler)

logger.warning("Important: This message should be logged")
logger.warning("This is a log entry for aprendendo")

"""
-> python-json-logger
- Cria um logging estruturado
- Da para facilmente customizar o formato dos logs, adicionar
metadados e fazer os logs mais facilmente lidos por maquinas
"""

new_logger = logging.getLogger(__name__)

stdout = logging.StreamHandler(stream=sys.stdout)
rename_fields = {"levelname": "log_level", "asctime": "timestamp", "name": "module"}

new_formatter = jsonlogger.JsonFormatter(string_format, rename_fields=rename_fields)

stdout.setFormatter(new_formatter)
new_logger.addHandler(stdout)

new_logger.warning("A Warning Message")
new_logger.error("An Error Message")
new_logger.critical("A Critical Message")

# Da para adicionar um valor extra em um log especifico usando
# "extra"
# new_logger.info("An Info Message", extra={"type": "common info"})

# Parei em "Logging Errors"
