function generate_noisy_data(f, x_min, x_max, num_samples, noise_level, factor)
  local data = {}

  -- Generate evenly spaced x values between x_min and x_max
  local step = (x_max - x_min) / (num_samples - 1)

  for i = 0, num_samples - 1 do
    local x = x_min + i * step
    local y = f(x)

    -- Add random noise to y (perturbation)
    local noise = (2 * math.random() - 1) * noise_level * math.exp(factor)
    local t = (x - x_min) / (x_max - x_min)
    y = y + noise * t

    table.insert(data, {x = x, y = y})
  end

  return data
end

function print_data(data)
  print([[\(x\) , \(y\) \\\midrule]])
  for _, point in ipairs(data) do
    print(string.format("%.2f , %.2f\\\\", point.x, point.y))
  end
end

function print_data(data)
  for _, point in ipairs(data) do
    print(string.format("%.2f, %.2f", point.x, point.y))
  end
end

-- print_data(generate_noisy_data(function(x) return x*x end, 0, 20, 200, 10, 1))
-- print_data(generate_noisy_data(function(x) return x*x end, 0, 20, 200, 10, 3))
print_data(generate_noisy_data(function(x) return 1/20*x*x*x end, 0, 20, 200, 10, 2))

