-- main.lua
-- 

function love.load ()
	OFFSETX = 256
	OFFSETY = 256
	image = love.graphics.newImage("assets/test.png")
end

function love.update()
	if gameIsPaused then
		return
	end
	
end

function love.draw()
	for Z = 0, 5 do
		for Y = 0, 10 do
			for X = 0, 5 do
				x = X * 64 + (Y % 2) * 64 / 2 + OFFSETX
				y = Y * 64 / 4 - Z * 64 / 2 + OFFSETY
				love.graphics.draw(image, x, y)
			end
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
