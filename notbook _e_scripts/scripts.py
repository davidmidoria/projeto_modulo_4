# os gráficos foram criados com intenção a criar respostas especificas para
# apresentação a qual foi solicitado para responder qualquer outra pergunta
# será necessario refatorar os gráficos a seguir  

import matplotlib.pyplot as plt
import pandas as pd


# lendo csv 
analise=pd.read_csv('../dados/dados_analise.csv')


  
# respondendo as perguntas feitas na descrição do projeto

quantidade_bugs=analise['qtda_bugs'][analise.index==analise.index.max()-1].max()-analise['bugs_corrigidos'][analise.index==analise.index.max()-1].max()
resposta_1=analise['horas_trabalhadas'][analise['semana']==4 ].sum()
resposta_2=analise['horas_trabalhadas'][analise['semana']==4 ].mean()
resposta_3=analise['bugs_corrigidos'][analise['semana']==4 ].sum()
resposta_4=analise['bugs_corrigidos'][analise['semana']==4 ].mean()
resposta_5=analise['tarefas_concluidas'][analise['semana']==4 ].sum()
resposta_6=analise['tarefas_concluidas'][analise['semana']==4 ].mean()
indicadores=['Total de Horas Trabalhadas','Média Diária de Horas Trabalhadas','total de Bugs Corrigidos','Média Diária de Bugs Corrigidos','Total de Tarefas Concluídas','Média Diária de Tarefas Concluídas','bugs a serem resolvidos']

respostas=pd.Series([resposta_1,resposta_2,resposta_3,resposta_4,resposta_5,resposta_6,quantidade_bugs],index=indicadores).apply(lambda x: round(x,1),)

pesquisa_7=pd.Series((analise['tarefas_concluidas'][analise['semana']==4]/analise['horas_trabalhadas'][analise['semana']==4]).to_list(),index=(analise['dia'][analise['semana']==4].to_list())).sort_values()

# grafico da ultima pergunta feita na descrição do projeto

def resposta_7():
    barras=pesquisa_7.index.to_list()
    valores=pesquisa_7.tolist()
    indice_maior_valor = valores.index(max(valores))
    cores = ['#909295' for _ in valores]
    cores[indice_maior_valor]='#5584bc'
    plt.figure(figsize=(10,4))
    for barra in plt.barh(barras, valores, color=cores):
                largura = barra.get_width()
                plt.text(largura/1.05, barra.get_y() + barra.get_height() / 2, str(largura), ha='right', va='center', fontsize=15,color='white')
    plt.title('tarefas concluidas por hora',fontdict={'fontsize': 20, 'color': '#5584bc', 'fontweight': 'bold', 'fontstyle': 'italic'}, loc='left')

    plt.xticks([]) 
    plt.gca().spines[['top','right','bottom','left']].set_visible(False) 
    plt.gca().tick_params(axis='y', colors='gray')
    plt.subplots_adjust(left=0.4, right=1.0)
    plt.show()

# gráfico de percentual de bugs não corrigidos

def relatorio_extra():
    analise['bugs_n_corrigidos']=analise['qtda_bugs']-analise['bugs_corrigidos']
    relatorio_bugs=(analise['bugs_corrigidos'].groupby(analise['semana']).sum()*100/(analise['bugs_n_corrigidos'][analise['dia']=='sabado'].values+analise['bugs_corrigidos'].groupby(analise['semana']).sum())).apply(lambda x: round(x,0))
    x = ['primeira','segunda','terceira','quarta'][::-1]
    y =100-relatorio_bugs[::-1]
    p=100
    plt.barh(x,p,color= '#909295' )

    for barra in plt.barh(x, y,color=['#B22222','#B22222','grey','grey']):
                largura = barra.get_width()
                plt.text(largura/1.05, barra.get_y() + barra.get_height() / 2, (f'{int(largura)}%' if largura>0 else ''), ha='right', va='center', fontdict={'fontsize': 15, 'color': 'white', 'fontweight': 'bold', 'fontstyle': 'italic'})

    plt.gca().spines[['top','right','bottom','left']].set_visible(False)
    plt.xticks([])
    plt.yticks(x,color='grey',fontweight='bold')
    plt.title('percentual de bugs não corrigidos por semana',loc='left',fontdict={'fontsize': 20, 'color': '#B22222', 'fontweight': 'bold', 'fontstyle': 'italic'})
    plt.grid(False)
    plt.text(3, 3, '0%',fontdict={'fontsize': 15, 'color': 'white', 'fontweight': 'bold', 'fontstyle': 'italic'})
    plt.text(3, 2, '0%',fontdict={'fontsize': 15, 'color': 'white', 'fontweight': 'bold', 'fontstyle': 'italic'})
    plt.show()

# gráfico do numero de tarefas concluidas
def queda_pr():
    a=analise['tarefas_concluidas'].groupby(analise['semana']).sum()
    c=a.to_list()
    a=analise['tarefas_concluidas'].groupby(analise['semana']).sum()
    c=a.to_list()
    b=a.index.tolist()
    plt.plot(b,c,color='grey')
    plt.scatter([2,3], [62.0,50.0], color='#B22222', marker='h', label='Pontos')
    plt.scatter([1,4], [64.0,34.0], color='black', marker='o', label='Pontos')
    plt.ylim(bottom=0,top=100)
    plt.gca().spines[['top','right']].set_visible(False)
    plt.xticks([1,2,3,4],['primeira','segunda','terceira','quarta'],color='grey')
    plt.annotate('(primeiro lay off)', xy=(2, 62.0), xytext=(2, 68),color='#B22222',fontsize=12,fontstyle= 'italic', arrowprops=dict(arrowstyle='->',mutation_scale=10, alpha=1,linewidth=1,color='#B22222'))
    plt.annotate('(segundo lay off)', xy=(3, 50.0), xytext=(3, 60),color='#B22222',fontsize=12, fontweight= 'bold', fontstyle= 'italic', arrowprops=dict(arrowstyle='->',mutation_scale=10, alpha=1,linewidth=1,color='#B22222'))
    plt.annotate('34 tarefas concluidas ', xy=(4,34.0), xytext=(4, 45),color='black',fontsize=12, fontweight= 'bold', fontstyle= 'italic', arrowprops=dict(arrowstyle='->',mutation_scale=10, alpha=1,linewidth=1,color='black'))
    plt.annotate('64 tarefas concluidas ', xy=(1, 64.0), xytext=(1, 75),color='black',fontsize=12, fontweight= 'bold', fontstyle= 'italic', arrowprops=dict(arrowstyle='->',mutation_scale=10, alpha=1,linewidth=1,color='black'))
    plt.yticks(color='grey')
    plt.gca().spines[['left','bottom']].set_color('gray')
    plt.title('queda no numero de tarefas concluidas\n ao longo das quatro semanas\n',color='#B22222',fontweight= 'bold',fontsize=15, fontstyle= 'italic')
    plt.show()

# gráfico do numero de horas trabalhadas 
def horas_trabalhadas():
    a=analise['horas_trabalhadas'].groupby(analise['semana']).sum()
    for barra in plt.bar(a.index.to_list(),a.to_list(),color=['grey','grey','darkred','darkred']):
            plt.text(barra.get_x()+0.4,barra.get_height()-2.5,  (f'{int(barra.get_height())}H'), ha='center', va='center', fontdict={'fontsize': 15, 'color': 'white', 'fontweight': 'bold', 'fontstyle': 'italic'})
    plt.gca().spines[['top','right','left']].set_visible(False)
    plt.xticks([1,2,3,4],['primeira','segunda','terceira','quarta'])
    plt.yticks([])
    plt.title('carga horária execessiva',color='#B22222',fontweight= 'bold',fontsize=15, fontstyle= 'italic',loc='left')
    plt.xlabel('semana')
    plt.show()

 