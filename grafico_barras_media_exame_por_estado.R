#setwd("diretorio_onde_estao_os_arquivos")
getwd()
media_estados <- read.table('media_exames_por_estado.txt', header = FALSE, sep = ",", dec = ".")
media_estados
library(ggplot2)
p<-ggplot(data=media_estados, aes(x= V1, y= V2)) +
  geom_bar(stat="identity", color = 'purple', fill = "mediumpurple") +
  xlab("Estado") + ylab("Média de exames")
p + ggtitle("Exames citopatológicos de colo do útero realizado pelo SUS \n em mulheres de 25 a 59 anos de 12/2008 a 12/2011 \n Média de exames normalizada pela população de interesse em cada estado") + theme(plot.title = element_text(hjust = 0.5)) +
geom_line() +
geom_hline(yintercept = mean(media_estados[,2]), color="darkmagenta", linetype="dashed")
mean(media_estados[,2])
