def fibo_by_nth(nth)
  case nth
    when 0 then
      [0]
    when 1 then
      [0, 1]
    when 2 then
      [0,0,1]
    else
      result = fibo_by_nth(nth-1)
      result << result[-2] + result[-1] + result[-3]
  end
end

puts fibo_by_nth(10)