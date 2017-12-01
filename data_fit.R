mydata=read.csv('results.csv',header=FALSE)
colnames(mydata)=c('degs','volts','fogs','time')
#mydata$degs=mydata$degs+0;
degs=unique(mydata$degs)
spread=rep(0,length(degs))
for(i in c(1:length(spread))){
  ix=which(mydata$degs==degs[i]);
  thyme=mydata$time[ix];
  thyme=thyme-min(thyme);
  dt=diff(thyme)
  fog=mydata$fogs[ix]
  dfog=(diff(fog));
  dfdt=dfog/dt;
  spread[i]=median(dfdt);
}
spread=spread;#*60;
macks=median(spread)*2;
ix=-c(1:length(spread));
t=pi/180*degs[-ix];
xc=cos(t);
xs=sin(t);
fit=lm(spread[-ix]~xc+xs);

# use the linear statistical model to find north
alfa=fit$coefficients[2];
betta=fit$coefficients[3];
B=fit$coefficients[1];
A=sqrt(alfa^2+betta^2);
phase_shift = atan2(betta,alfa);
phase_shift = pi/2-phase_shift;
faze=phase_shift*180/pi;
root=(180-asin(-B/A)*180/pi-faze)%%360;

cat(sprintf("North is located at: %.2f degrees relative.\n",root));

# using a linear model and fit to find north... less efficient
pred=predict(fit,data=degs);
north_ix=which(diff(pred>0)<0);
north_arry=c(north_ix,north_ix+1);
north_fit = lm(pred[north_arry]~degs[north_arry]);
north = -north_fit$coefficients[1]/north_fit$coefficients[2];

pdf('fit.pdf')
plot(degs[-ix],spread[-ix],xlab='Relative Rotation Angle',ylab='Counts per Second');
lines(degs[-ix],pred,col='blue');
points(c(north,root),c(0,0),col='red',pch=20);

points(c(c(0,270,180,90)-faze),rep(B,4),pch='*');
lines(degs[-ix],A*sin(t+phase_shift)+B,col='red');
dev.off()