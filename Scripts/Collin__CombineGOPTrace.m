%CombineGOPTrace.m
%Collin Daly
%10:59 27APR2016
%recombines video frames from practice attempt into a video based on GOP 
%values.  Outputs from neural network (NAR) are recombined to form a trace
%file which is run through the EPON simulator.

%Inputs:  delayi,delayb,delayp,  yi,yb,yp
root = ['C:\Users\cd03292\Google Drive\1- Video Prediction '...
                'Simulations\Run0\NAR_HarryPotter\'];
savepath = 'E:\2016 Research\EPON Sim\';
% traceFile = 'E:\2016 Research\EPON Sim\TraceHP_Q10.txt'
% traceFile = 'E:\2016 Research\EPON Sim\TraceHP_Q20.txt'
% traceFile = 'E:\2016 Research\EPON Sim\TraceHP_Q30.txt'
traceFile = 'E:\2016 Research\EPON Sim\TraceHP_Q40.txt'

% iaddress = [root,'NAR_I_10_v4_11_6_18Jan2016_2220.mat'];
% baddress = [root,'NAR_B_10_v4_11_6_18Jan2016_2219.mat'];
% paddress = [root,'NAR_P_10_v4_11_6_18Jan2016_2220.mat'];
 
% iaddress = [root,'NAR_I_20_v4_11_6_19Jan2016_0545.mat'];
% baddress = [root,'NAR_B_20_v4_11_6_19Jan2016_0545.mat'];
% paddress = [root,'NAR_P_20_v4_11_6_19Jan2016_0545.mat'];

% iaddress = [root,'NAR_I_30_v4_11_6_19Jan2016_1115.mat'];
% baddress = [root,'NAR_B_30_v4_11_6_19Jan2016_1115.mat'];
% paddress = [root,'NAR_P_30_v4_11_6_19Jan2016_1115.mat'];

iaddress = [root,'NAR_I_40_v4_11_6_19Jan2016_1613.mat'];
baddress = [root,'NAR_B_40_v4_11_6_19Jan2016_1613.mat'];
paddress = [root,'NAR_P_40_v4_11_6_19Jan2016_1613.mat'];

% savefile = [savepath,'HP_Q10_11_6.txt'];
% savefile = [savepath,'HP_Q20_11_6.txt'];
% savefile = [savepath,'HP_Q30_11_6.txt'];
savefile = [savepath,'HP_Q40_11_6.txt'];

load(iaddress,'y');
yi= cell2mat(y);
load(iaddress,'Delay');
delayi = Delay;
load(baddress,'y');
yb= cell2mat(y);
load(baddress,'Delay');
delayb = Delay;
load(paddress,'y');
yp= cell2mat(y);
load(paddress,'Delay');
delayp = Delay;

length_i = length(yi);
length_b = length(yb);
length_p = length(yp);

countI = 2;%becuase next frame is I#2 at B#21 for GoP#1Frame24
countB = 1;
countP = 1;
totalLength = (length_i + length_b + length_p);
overall=zeros(2,totalLength);

for i = 1:totalLength
    
    gop = mod(i,24);
    if gop == 8
        %append p1
        if countP > delayp
            overall(1,i) = round(yp(countP-delayp));
            overall(2,i) = 'P';
        end
            countP = countP + 1;
            continue;
    elseif gop == 16
        %APPEND P2
        if countP > delayp
            overall(1,i) = round(yp(countP-delayp));
            overall(2,i) = 'P';
        end
            countP = countP + 1;
            continue;
    elseif gop == 0
        %append next I
        if countI > delayi
            overall(1,i) = round(yi(countI-delayi));
            overall(2,i) = 'I';
        end
            countI = countI + 1;
            continue;
    else
        %append B
        if countB > delayb
            overall(1,i) = round(yb(countB-delayb));
            overall(2,i) = 'B';
        end
            countB = countB + 1;
    end
end

filename = fopen(traceFile,'rt');
% filename1 = fopen('E:\2016 Research\EPON Sim\test1.txt','w');
filename2 = fopen(savefile,'w');
countHash = 0;
count = 1;
 while (count <= totalLength)
 
    line = fgetl(filename);
    if (line(1) == '#')
        fprintf(filename2,line);
        fprintf(filename2,'\r\n');
        
%         fprintf(filename1,line);
%         fprintf(filename1,'\r\n');
        countHash = countHash + 1;
        continue;
    else
        fprintf(filename2,line);
        fprintf(filename2,'\t');
        %fprintf(filename2,'%d',overall(1,count));
        fprintf(filename2,num2str(overall(1,count)));
        fprintf(filename2,'\r\n');
        
        
%         fprintf(filename1,line);
%         fprintf(filename1,'\t');
%         fprintf(filename1,'%d',overall(1,count));
%         %fprintf(filename1,num2str(overall(1,count)));
%         fprintf(filename1,'\r\n');
        count = count + 1;
    end

 end

fclose('all');
        
        
        
        
        