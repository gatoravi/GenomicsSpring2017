t <- read.table("normalized_matrix.tsv")
m1 <- as.matrix(t[, 2:ncol(t)])
m2 <- t(m1)
mydata <- m2
d <- dist(mydata, method = "euclidean")
fit <- hclust(d, method="ward")
png("dendogram.png")
plot(fit)
dev.off()
