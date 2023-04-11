'''Jogo da Historia de um casamento muito louco'''
# primeiro os dados dos noivos
# perfil dos noivos 
# contar a historia dos noivos 
#finalizar com o pastor sendo chamado pelo sistema para fazer o casamento 

d = "Deus"
nome1 = "Lucas"
nome2 = "Ana Rosa" 
Na = 'Narrador'
orla = 'Orla do Bessa'
inicio = '2021'
mes_historia = "Janeiro"
mes_inicio = 'Fevereiro'
ce = 'Célula EMAUS'
sol = "Salvadora Solange"
wa = "Cabeça Branca"
gi = 'Ana Gimmena'
gu = 'Pr. Gusto'
casamento = '30 de Março'
pascoa = ' Domingo de Pascoa'
casal = 'LUCAS & ANA ROSA'



def ler_escolha():
    escolha = input(f'{player_1}, Agora é sua vez, Por favor Digite "sim" ou "não": ')
    while escolha not in ['sim', 'não']:
        escolha = input(f'{player_1}, Agora é sua vez, Por favor Digite "sim" ou "não": ')
    return escolha


while True:
    player_1 = input("Digite seu Nome: ")
    print('')
    print(f'Parabéns {player_1}, você foi cadastrado com sucesso, se prepare para entrar na aventura "era só uma corrida na orla".') #cadastro do leitor
    print(f'Bem-vindo {player_1}, ao casamento de {nome1} e {nome2}, gostaria de saber mais sobre como chegamos ate o dia de HOJE?')# inicio da leitura do romance
    print('')

    entrada = ler_escolha()

    if entrada == 'sim':
            print('')
            print(f'Parabéns pela Coragem, {player_1}, agora vou me apresentar, meu nome é {Na}.')
            print(f'Agora que você me conheçe, te convido a conhecer os personagens dessa Aventura e o Prefácio dessa louca aventura, {player_1}, você está preparado?.')
            print(' ')
            
            entrada = ler_escolha()
            
            if entrada == 'sim':
                print('')
                print(f'{d} =>  é o todo poderoso que controla tudo, inclusive o destino.')
                print(f'{orla} =>  geralmente local usado para fazer corridas')
                print(f'{nome1} => é um rapaz que só queria correr na {orla}. ')
                print(f'{nome2} => pessoa esperta que está devendo uma corrida na {orla}, ao {nome1} ')
                print(f'Dona {sol} => Mãe do {nome1}, e pessoa incrivel, que sempre agradeçeu por tudo na vida')
                print(f'{wa} => Apelido do pai do {nome1}, cujo o nome real é Wanderley, porém a grande maioria conhece como Cabeça Branca.')
                print('')
            
                entrada = ler_escolha()

                if entrada == 'sim':
                    
                    print('')
                    print(f'Era uma vez...')
                    print('...')
                    print(f'O ano era {inicio} e o mês era {mes_historia}, esse foi o ano dos concurso policiais no Brasil, e enquanto {nome1} estava se preparando para os concursos de carreiras policiais,')
                    print(f'esse tal de {nome1}, estava recém divorciado, e ele não queria namorar nem tão cedo, devido a um divorcio traumático,')
                    print(f'sua mãe dona {sol} disse para o {nome1},("- {nome1}, Eu não quero conhecer nenhuma namorada sua, seu divorcio já foi muito traumático para mim." ).')  
                    print(f'enquanto isso, do outro lado da cidade no bairro dos Bancários, existia uma pessoa que seria a responsável por aplicar o maior golpe de todos...') 
                    print(f'o nome dela é: {nome2}, ela conseguiu aplicar um golpe tão grande, que daria origem a expressão conhecida como: "O golpe tá ai, cai quem quer..."')
                    print('')
                    print(f'{player_1}, agora que ja conheçe o inicio na historia, você deseja saber mais ?.')
                    print(' ')
                        
                    entrada = ler_escolha()
            
                    if entrada == 'sim':
                            
                        print('')
                        print(f'{player_1}, nossa como você é fofoqueiro, (hahahaha..., brincadeira), então sem mais delongas vamos aos fatos dessa aventura emocionante.')
                        print(f'o  uma segunda-feira qualquer de {mes_inicio}, onde o {nome1}, voltando da academia, sozinho e triste por não ter amigos na cidade teve a grande ideia...')
                        print(f'vou add algumas pessoas da academia assim posso fazer novos amigos e ainda terei companhia pra treinar, pensou o {nome1}.')
                        print(' ')
                            
                                    
                        entrada = ler_escolha()
            
                        if entrada == 'sim':
                            print(' ')
                            print (f'então o {nome1} foi add varias pessoas da sua academia, entre elas estava uma tal de {nome2}, que também foi add.')
                            print(f'e o dia seguinte chegou, e o {nome1} começou a conversar com varias pessoas que add no dia anterior e sem fazer a menor ideia acabou combinando com a {nome2} de correr {orla} na quarta-feira.')
                            print(' ')
                                        
                            entrada = ler_escolha()
            
                            if entrada == 'sim':
                                print('')
                                print(f'chegou o grande dia, o primeiro dia de um golpe grande aplicado pela {nome2}, que o {nome1} caiu feito patinho heheh...')
                                print(f'o que a {nome2} e o {nome1} não sabiam era, que toda essa historia já tinha sido escrita pelo autor da vida o {d} de Israel.')
                                print(f'então na quarta eles se encontraram e conversaram um pouco, e lembrando que era para correr mas a {nome2} chamou o {nome1} para sentar na {orla} conversar e os dois foram se conhecendo.')
                                print(f' depois de muito conversarem, a {nome2} ficou curiosa com a tatoo que o {nome1} tinha no braço, e perguntou o significado dela,')
                                print('')
                                    
                                entrada = ler_escolha()
            
                                if entrada == 'sim':
                                        
                                    print('')
                                    print(f'foi nesse momento que o {nome1}, aproveitou para jogar seu charme e tirar onda.... hahahah... o {nome1}, fez pose para mostrar os musculos do braço, e começou explicar o sentido da tatoo...')
                                    print(f'nesse momento a {nome2} pensou, "o que esse fracote está tentando me mostrar nesse braço fracote, mas vou deixar ele continuar só para ver qual é a historia dessa tatoo"(pensou a {nome2}).')
                                    print(f'quanto o {nome1}, terminou de explicar e contar de suas aventuras em MANAUS, a {nome2} disse: "-Eu tenho um amigo que também foi para manaus trabalhar", e conversa vem conversa vai.')
                                    print(f'os dois descobrem que ambos moravam em BRASILIA e nunca tinham cruzado antes em Brasilia, mas nesse momento já passa da 00:00 e os dois decidiram se encontrar outro dia para tentar correr, ')
                                    print(f'pensava o {nome1} com sua doce inocência.')
                                    print('')
                                        
                                    entrada = ler_escolha()
                                        
                                    if entrada == 'sim':
                                            
                                        print('')
                                        print(f'no seu terceiro encontro o {nome1} pensou "esse vai ser o terceiro encontro com essa tal {nome2}, ate hoje não corremos, mas ja não vejo minha vida sem o sorriso dela".')
                                        print(f'foi quando o {nome1} teve uma grande ideia, chamou a {nome2} para ir na praia ver a lua, e o {nome1} ja tinha planejado tudo bem certinho, levou a luneta a caixa de som.')
                                        print(f'o {nome1} ligou para a {nome2}, e falou:-{nome2} se prepara por que hoje vou ter levar para ver a lua.')
                                        print(f'e foi assim em uma noite de lua cheia que {nome1} deu um banho de mar na {nome2}, e começaram a ter um relacionamento, mas até então nada de namoro, apenas troca de fluidos salivares sem compromisso.')
                                        print('')        
                                            
                                        entrada = ler_escolha()
                                            
                                        if entrada == 'sim':
                                                
                                            print('')
                                            print(f'Passados alguns meses nessa enrolação de ninguem querer compromisso, a {nome2}, ligou para {nome1} (cel):"- {nome1}, Eu estou te ligando por que queria saber qual é a sua?, quero saber se você vai me namorar ou vai sair fora?')
                                            print(f'Foi então, depois dessa leve pressão e como {nome1}, ja tinha certeza que não poderia mais viver sem essa morena linda, correu para tomar uma atitude e foi logo pedindo ela em namoro,')
                                            print(f'a {nome2}, aceitou o pedido de namoro então, foi assim que o {nome1} e {nome2}, iniciaram um namoro,')
                                            print(f'mas o que a {nome2} não fazia ideia era que o {nome1}, não gostava de responder midias sociais, (obs: ele é assim ate hoje, hehe...), ')
                                            print(f'e devido a essa mania do {nome1}, de não responder as midias sociais, foi o motivo da primeira briga porém, abriu margem para o {nome1}, querer apresentar seu pai o {wa},')
                                            print(f'para que a {nome2} pudesse entender o motivo pelo qual o {nome1} não gostava de redes sociais.')
                                            print(f'contudo, a {nome2}, mal sabia que o mais difícil seria conhecer a mãe de {nome1}, pois como a dona {sol} já tinha tido não queria nem papo.')
                                            print(f'más como toda mulher sábia, a {nome2}, havia decidido, conquistar a dona {sol}, pela barriga.(hehehe)')
                                            print(f'foi então que a {nome2} teve a ideia de comprar empadinhas mais famosas de João Pessoa (vou nem dizer que era Empadinha BARNABÉ, não estou escrevendo pra fazer propaganda),') 
                                            print(f'todas as vezes que se encontrava com seu namorado pedia para que ele entregasse a dona {sol}.')
                                            print(f'e foi assim de empadinha em empadinha que um dia a dona {sol} decidiu conhecer a então namorada de seu filho {nome1},')
                                            print(f'e depois que a dona{sol}, conheceu a {nome2},  se gostaram muito, e sempre ficavam marcando irem na praia juntas e a dona {sol} sempre chamava a {nome2} para os almoços de domingo,')
                                            print(f'ficaram tão amigas e fizeram uma descoberta fora do comum, a {nome2}, descobriu que a dona {sol}, havia sido professora do primo da {nome2}, no jardim de infância')
                                            print(f'porém os planos de {d}, são misteriosos e não fazem sentido ao entendimento humano, pois após 4 meses que {nome2}, havia conhecido a dona {sol}, {d} levou a dona {sol} para seus braços,')
                                            print(f'e houve uma completa mudança na vida de todos,')
                                            print('')
                                            print(f'Então, {player_1}, gostando?')
                                            print('')
                                            
                                            entrada = ler_escolha()
                                            
                                            if entrada == 'sim':
                                                print('')
                                                print(f'Nossa, {player_1}, você é curioso mesmo... ...sem problemas hoje pode, vamos seguir com a nossa aventura')
                                                print('')
                                                print(f'Então após o falecimento da dona {sol}, o sr.{wa} ficou muito abalado, e muito perdido, chegou a entrar em um relacionamento tão tóxico que o {wa}, chegou a expulsar o {nome1} de casa,')
                                                print(f'porém tudo isso ja fazia parte do plano de {d} para que o casal {nome1} e o {nome2}, pudesse estar hoje se casando, eu {Na}, vou te explicar melhor,')
                                                print(f'o sr. {wa}, viajou para Brasilia pois precisava cuidar de sua saúde, e foi quando o {wa} descobriu uma suspeita de câncer, e o {wa} ficou preocupado, achando que iria morrer,')
                                                print(f'foi então que ele teve a brilhante ideia de expulsar seu filho o {nome1},')
                                                print(f'pois o {wa}, pensou "- eu expulso o {nome1} de casa, ele vai para casa da namorada a {nome2}, e eles acabam casando porque a {nome2} ama muito ele,')
                                                print(f'então se eu morrer meu filho não vai ficar sozinho no mundo" pensou sozinho e logo quando voltou de Brasilia colocou seu plano em pratica,')
                                                print(f'o problema do plano que o {wa} decidiu colocar em pratica, foi só um, ele não perguntou se a {nome2} queria casar com o {nome1}, e se o {nome1} queria casar com {nome2}, então isso gerou alguns conflitos,')
                                                print(f'porém os planos de {d}, sempre são maiores, eu {Na} posso afirmar que se não fosse isso, esses dois estariam ate hoje só no marasmo do namoro, sem a menor pressa para casar.')
                                                print('')
                                                print(f'Você acha que acobou? ainda tem mais, mas {player_1}, fique tranquilo(a) estamos no último cap. desse livreto')
                                                print('')
                                                
                                                entrada = ler_escolha()
                                            
                                                if entrada == 'sim':
                                                    print('')
                                                    print(f'Essa fase da aventura eu o {Na} custumo chamar de "buscando  ter mais intimidade com {d}".')
                                                    print('')
                                                    print(f'Nesse nomento o  casal {nome1} e {nome2} já estavam morando juntos, porém ambos sabiam que estavam em pecado aos olhos de {d},')
                                                    print(f'e foi nesse momento que todos os presentes e a {ce} entram em cena, por que foi devido a varias conversas com a {gi} e depois de um gabinete com o {gu}, que o casal {nome1} e {nome2} decidiram casar.')
                                                    print(f'{player_1} você sabia que nosso querido casal, realizou o casamento civil no ultimo dia {casamento}, e hoje o nosso amado {gu} irá celebrar a festa e o casamento religioso.')
                                                    print('')
                                                    print('')
                                                    
                                                    entrada = ler_escolha()
                                                    
                                                    if entrada == 'sim':
                                                        print('')
                                                        print(f'{player_1}, para nós (eu o {Na}, o casal {casal}) é um prazer ter você aqui, agora o nosso livreto chegou ao final, aproveite a festa.')
                                                    
                                                    
                                                
                                            
                                                    

        
    elif entrada == 'não':
            print(f'Você perdeu a oportunidade de conhecer um pouco mais da nossa historia, mas obrigado por estar presente nesse dia tão especial para nós {nome1} e {nome2}.')

    else:
            print('Você não digitou nem "sim" e nem "não".')

    print(f'Se, você chegou até aqui é sinal que o nosso amado {gu} irá realizar a Cerimonia de Casamento em poucos minutos.')
    print('')       
    print(f'Obrigado a todos que compareceram nesta celebração, e tenham uma ótima  {pascoa} amanhã...')
    print(f'')
    print('')
    print('')
    print('De sorte que, assim como a igreja está sujeita a Cristo, assim também as mulheres sejam em tudo sujeitas a seus maridos.')
    print('Vós, maridos, amai vossas mulheres, como também Cristo amou a igreja, e a si mesmo se entregou por ela.')
    print('Efésios 5:24,25')