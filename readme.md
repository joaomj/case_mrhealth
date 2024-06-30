# Case Mr. Health

Case de estudos para a Data Lakers.

## Contexto

A DataLakers foi contratada pela MR. HEALTH para desenvolver um modelo preditivo simplificado que possa auxiliar a MR HEALTH na otimização a gestão de estoques de suas unidades. Utilizando dados históricos de vendas, o modelo deverá ser capaz de prever a demanda futura, permitindo um planejamento mais eficiente das quantidades a serem estocadas em cada unidade.

### A Mr. Health
A MR HEALTH é uma rede de “Slow-Food” presente na região sul e com aproximadamente 50 unidades.

Foi fundada há 5 anos pelo chef João Silva, e desde lá vem crescendo de forma exponencial. Com a pandemia, a rede teve que se adequar e expandir sua atuação on-line.

A MR HEALTH é o sonho de João Silva em poder oferecer alimentação saudável e acessível a todos. Porém após ter passado o período da pandemia, vem refletindo sobre como escalar seu negócio para outros estados, já que necessita ter as informações para tomada de decisão de forma mais rápida em suas mãos e poder adotar modelos estatísticos para gestão dos estoques de suas unidades.

## Entregáveis

### Etapas do projeto
1. Explorar os dados históricos de vendas fornecidos nos arquivos "PEDIDO.CSV", "ITEM_PEDIDO.CSV" e “ITENS.CSV”.
2. Verificar a qualidade dos dados, identificar possíveis problemas e realizar tratamentos necessários.
3. Realizar uma análise descritiva para entender o comportamento das vendas, identificar padrões sazonais e outras características relevantes.
4. Selecionar um modelo adequado para previsão de demanda, como regressão linear ou regressão logística, com base na análise exploratória e nas características dos dados.
5. Dividir os dados em conjuntos de treinamento e teste.
6. Treinar o modelo utilizando os dados históricos de vendas e realizar a validação para avaliar seu desempenho.
7. Avaliar o desempenho do modelo com base em métricas apropriadas, como erro médio absoluto (MAE) ou erro médio quadrático (MSE).
8. Fornecer recomendações para a MR HEALTH com base nos resultados obtidos, incluindo insights sobre possíveis melhorias no processo de gestão de estoques.

**Entregáveis Esperados**
Código fonte em Python, contendo as etapas de análise exploratória de dados e desenvolvimento do modelo preditivo.

## Requisitos
- Ambiente **conda** (miniconda3) em Linux (WSL) conectado ao VS Code rodando no Windows.

### Como ativar o ambiente de desenvolvimento (bash)
Execute o seguinte script após instalar o conda:

 ```python
# Create a new environment and install Conda packages
conda create --name my_env --file requirements.txt

# Activate the new environment
conda activate my_env
 ```
 
## Contributing 

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)