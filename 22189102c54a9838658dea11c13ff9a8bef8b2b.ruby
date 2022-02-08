#find the secret 

n=gets.to_i
n.times do
    h={}
    s = gets.chomp.chars
    s.each do |c|
        if c=~/[a-z]/i
            if h[c].nil?
                h[c]=0
            end
            h[c]+=1
        end
    end
    o=""
    h.each do |k,v|
        if v>1
            o+=k
        end
    end
    if o==""
        puts "NONE"
    else
        puts o
    end
end
