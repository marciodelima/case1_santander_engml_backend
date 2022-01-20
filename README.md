# Case 1 - APP Back-End - Rest/API - F1rst
## DataMaster - Engenharia de ML - JAN/2022
Esse GIT destina-se a aplicação Rest/API que expõe o modelo de ML como um serviço para ser chamado pelo Front-End.

### Objetivo
Através dos dados informados (13 informações) indicar se o paciente tem ou não a probabilidade de ter uma doença cardíaca. 

### Uso
Ferramenta de simulação para médicos clínicos e/ou laboratórios para indicar um paciente para um tratamento especializado o mais rápido possível. 

### Escopo
Para o alcance do objetivo acima, foi criado 2 aplicações de arquitetura de micro-serviços, conforme abaixo. As aplicações rodam em containers no AKS e seu build e deploy ocorrem via Azure DEVOPS. 
- Web-Site: Foi criado uma APP Web, onde o usuário possa digitar as informações necessárias e clicar no botão “Verificar” para obter o resultado; A página WEB exibirá um Sim junto com a probabilidade ou um Não; 
- App de back-End: Essa aplicação expõe o modelo de ML (pkl) do case como um Web-Service REST, tornando-o uma API para servir a APP Web.
- A parte de infra-estrutura de Cloud (Azure) foi feita em Terraform (InfraAsCode)

### Ferramentas e Algoritmos
Python, FastAPI, Sklearn, Pandas, RandomForest

### Desenho

![Desenho de Solução](https://github.com/marciodelima/case1_santander_engml_geral/blob/main/desenho.png)
