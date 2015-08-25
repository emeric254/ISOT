-- main.lua
-- 

function love.load ()
	image = love.graphics.newImage("test.png")
end

function love.update()
	if gameIsPaused then
		return
	end
	
end

function love.draw()
	for j = 0, 5 do
		for i = 0, 5 do
			x = i * 64 + (j % 2) * 64 / 2
			y = j * 64 / 4
			love.graphics.draw(image, x, y)
		end
	end
end

function love.keypressed(key)
	if key == 'escape' then
		love.event.push('quit')
	end
end

function love.focus(f)
	if not f then
		print("lost focus")
	else
		print("get focus")
	end
	gameIsPaused = not f
end

function love.quit()
	print("goodbye")
end
