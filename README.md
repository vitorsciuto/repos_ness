# 🐉 Dashboard Monstro do Lago Ness

Um dashboard interativo desenvolvido em Streamlit para acompanhar e contabilizar interações do Monstro do Lago Ness por matéria e semana.

## 🚀 Funcionalidades

- **Contadores Interativos**: Botões para incrementar interações (+1, +5, +10, ou valor personalizado)
- **Visualizações Avançadas**: Gráficos de pizza, barras e linhas temporais
- **Análise por Período**: Divisão por semanas (Semana 1, 2 e 3)
- **Múltiplas Matérias**: Suporte a 4 matérias diferentes
- **Histórico Completo**: Registro de todas as interações com timestamp
- **Persistência de Dados**: Dados salvos automaticamente em arquivo JSON
- **Interface Responsiva**: Layout adaptável com abas organizadas

## 📊 Matérias Incluídas

1. **Análise de Dados**
2. **Circuitos Digitais**
3. **Desenvolvimento de Software**
4. **Fenômenos de Transporte**

## 🛠️ Instalação

1. Clone o repositório ou baixe os arquivos
2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute o dashboard:
```bash
streamlit run dashboard_ness.py
```

## 📈 Como Usar

### Controles Principais (Sidebar)
- **Selecione a Matéria**: Escolha qual matéria deseja incrementar
- **Selecione a Semana**: Defina em qual semana registrar a interação
- **Botões de Incremento**: Use +1, +5, +10 ou valor personalizado
- **Reset**: Limpe todos os dados se necessário

### Abas do Dashboard

#### 📊 Visão Geral
- Métricas principais (total geral e por semana)
- Cards individuais por matéria
- Visão consolidada dos dados

#### 📈 Gráficos
- **Gráfico de Pizza**: Distribuição percentual por matéria
- **Gráfico de Barras**: Comparação total entre matérias
- **Barras Empilhadas**: Análise por semana e matéria

#### 📋 Tabela Detalhada
- Tabela completa com todos os dados
- Linha de totais destacada
- Estatísticas adicionais (matéria mais ativa, semana mais ativa, média)

#### 📜 Histórico
- Registro cronológico de todas as interações
- Filtros por matéria e semana
- Gráfico de evolução temporal

## 💾 Persistência de Dados

Os dados são automaticamente salvos no arquivo `ness_data.json` e incluem:
- Contadores por matéria e semana
- Histórico completo de interações
- Timestamp da última atualização

## 🎨 Características Técnicas

- **Framework**: Streamlit
- **Visualizações**: Plotly Express/Graph Objects
- **Dados**: Pandas DataFrames
- **Persistência**: JSON
- **Responsividade**: Layout em colunas adaptável
- **Estilização**: CSS customizado

## 📱 Interface

O dashboard possui uma interface moderna e intuitiva com:
- Sidebar para controles principais
- Sistema de abas para organização
- Métricas destacadas
- Gráficos interativos
- Tabelas formatadas
- Histórico detalhado

## 🔧 Personalização

Você pode facilmente:
- Adicionar novas matérias editando a lista no código
- Modificar os valores de incremento
- Personalizar cores e estilos no CSS
- Adicionar novas visualizações

## 📊 Exemplo de Uso

1. Selecione "Análise de Dados" na sidebar
2. Escolha "Semana 1"
3. Clique em "+5" para adicionar 5 interações
4. Veja os dados atualizados em tempo real
5. Explore as diferentes abas para análises detalhadas

---

**Desenvolvido para acompanhar as interações do Monstro do Lago Ness de forma organizada e visual! 🐉**
