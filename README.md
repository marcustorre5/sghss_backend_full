# SGHSS – Sistema de Gestão Hospitalar, Saúde e Serviços  
**Backend em Django + Django REST Framework**

O SGHSS é uma API REST desenvolvida para apoiar o gerenciamento de entidades fundamentais do ambiente de saúde: **Pacientes**, **Profissionais de Saúde** e **Consultas**.  
Este repositório contém toda a implementação do backend, incluindo arquitetura, endpoints, autenticação e documentação.

---

# 📌 1. Sobre o Projeto

O sistema foi projetado para atender às necessidades de um ambiente hospitalar simplificado, permitindo:

- Registro completo de **pacientes**  
- Cadastro e gerenciamento de **profissionais de saúde**  
- Controle e agendamento de **consultas médicas**  
- **Autenticação via JWT** para proteger operações sensíveis  
- Integração com **PostgreSQL**  

O foco principal é demonstrar organização, modelagem, arquitetura limpa e boas práticas de desenvolvimento backend.

---

# 🛠 2. Tecnologias Utilizadas

### **Linguagem & Framework**
- Python 3.13  
- Django 5.x  
- Django REST Framework (DRF)

### **Autenticação**
- SimpleJWT (tokens de acesso e refresh)

### **Banco de Dados**
- PostgreSQL 16+

### **Ferramentas de Desenvolvimento**
- Visual Studio Code  
- Postman  
- Ambiente virtual `venv`  

---

# 📁 3. Estrutura do Projeto

A aplicação segue a estrutura padrão Django, com organização modular:

```
sghss_backend_full/
│── core/
│ ├── migrations/
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── serializers.py
│ ├── urls.py
│ ├── views.py
│
│── sghss_backend/
│ ├── settings.py
│ ├── urls.py
│ ├── asgi.py
│ ├── wsgi.py
│
│── venv/
│── iniciar_sghss.bat
│── manage.py
│── requirements.txt

```
### **Resumo dos Diretórios**
- `core/` → Aplicação principal (entidades e lógica de negócio)  
- `sghss_backend/` → Configurações gerais do projeto Django  
- `migrations/` → Histórico de modificações do banco  
- `manage.py` → Ferramenta administrativa  
- `requirements.txt` → Dependências do projeto  

---

# ⚙️ 4. Instalação e Execução

### **4.1. Clone o repositório**
```bash
git clone https://github.com/marcustorre5/sghss_backend_full
```
cd sghss_backend_full

Crie o ambiente virtual
python -m venv venv
venv\Scripts\Activate.ps1

4.3. Instale as dependências
pip install -r requirements.txt

4.4. Configure o PostgreSQL

Configuração padrão utilizada:

````
HOST: localhost
PORT: 5432
USER: postgres
PASSWORD: 250250
NAME: postgres
````

4.5. Execute as migrações
python manage.py migrate

4.6. Crie um usuário administrador
python manage.py createsuperuser

4.7. Inicie o servidor
python manage.py runserver


Acesse em:
http://127.0.0.1:8000/

# 🔐 5. Autenticação JWT

A API utiliza JSON Web Tokens (JWT).

Obter token de acesso
POST /api/token/

Renovar token
POST /api/token/refresh/

Enviar token no header
Authorization: Bearer SEU_TOKEN

# 📡 6. Endpoints Disponíveis
```
6.1. Pacientes – /api/pacientes/
Método	Descrição
GET	Listar todos
POST	Criar paciente
PUT/PATCH	Atualizar dados
DELETE	Excluir paciente
6.2. Profissionais – /api/profissionais/
Método	Descrição
GET	Listar profissionais
POST	Registrar profissional
PUT/PATCH	Alterar dados
DELETE	Remover
6.3. Consultas – /api/consultas/
Método	Descrição
GET	Listar consultas
POST	Criar consulta
PUT/PATCH	Atualizar consulta
DELETE	Excluir consulta
```
# 🧪 7. Testes com Postman

Todos os endpoints foram testados utilizando o Postman, incluindo:

Autenticação JWT

Testes de acesso autorizado

CRUD completo de todas as entidades


# 🚀 8. Scripts Úteis
Inicialização rápida (Windows):
iniciar_sghss.bat


Ele ativa a venv e executa automaticamente o servidor Django.

```
Autor:

Marcus Torres
Projeto acadêmico — Desenvolvimento Back-end.
````
