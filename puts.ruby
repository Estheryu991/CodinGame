n = gets.to_i
*,a,b,c = gets.split(" ").map(&:to_i)

if b-a == c-b
    puts c+c-b
elsif b/a == c/b
    puts c * (b/a)
end
