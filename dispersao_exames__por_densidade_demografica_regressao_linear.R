#setwd("diretorio_onde_estao_os_arquivos")
media_estados <- read.table('media_exames_por_estado_com_densidade_demografica.txt', header = FALSE, sep = ",", dec = ".")
media_estados
library(ggplot2)
library(ggrepel)
p<-ggplot(data=media_estados, aes(x= V3, y= V2)) +
  geom_point(stat="identity", color = 'purple', fill = "purple") +
  xlab(expression(paste("Densidade populacional (hab/km"^"2",")"))) +  ylab("Média de exames")
p + ggtitle("Exames citopatológicos de colo do útero realizado pelo SUS \n em mulheres de 25 a 59 anos de 12/2008 a 12/2011 \n Média de exames e densidade populacional") + theme(plot.title = element_text(hjust = 0.5)) + 
geom_text_repel(label= media_estados[,1], nudge_x = 0.2, nudge_y = 0.2) 

#excluindo os outliers do modelo linear
media_estados2 <- subset(media_estados, !(media_estados[,1]  %in% c("AM","MA","PA", "AP")))
media_estados2

p<-ggplot(data=media_estados, aes(x= V3, y= V2)) +
  geom_point(stat="identity", color = 'purple', fill = "purple") +
  xlab(expression(paste("Densidade populacional (hab/km"^"2",")"))) +  ylab("Média de exames")
p + ggtitle("Exames citopatológicos de colo do útero realizado pelo SUS \n em mulheres de 25 a 59 anos de 12/2008 a 12/2011 \n Média de exames e densidade populacional") + theme(plot.title = element_text(hjust = 0.5)) + 
geom_smooth(data=media_estados2, aes(x= V3, y= V2), method  = 'lm', interval = "confidence", level = 0.95) +
geom_text_repel(label= media_estados[,1], nudge_x = 0.3, nudge_y = 0.3)  
