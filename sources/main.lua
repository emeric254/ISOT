-- main.lua
--

function love.load()
   love.graphics.setNewFont(12)
   love.graphics.setBackgroundColor(255,255,255)
   love.graphics.setBlendMode("alpha")
   --
   text = "Hello World"
   --
   x_offset = 0
   y_offset = 0
   wanted_x_offset = 0
   wanted_y_offset = 0
   offset_frames = 60
   --
   tile_size = 32
   image = love.graphics.newImage("assets/default_cube.png")
   --
   cube = {
        {0, 1, 1, 1, 0},
        {1, 1, 1, 1, 1},
        {1, 1, 1, 1, 0},
        {1, 1, 1, 1, 0},
        {1, 1, 1, 1, 0},
        {1, 1, 1, 1, 0},
        {1, 1, 1, 1, 0},
        {1, 1, 1, 1, 0},
        {1, 1, 1, 1, 0},
        {1, 1, 1, 1, 0},
        {1, 1, 1, 1, 0}
    }
    --
    sounds = {}
    --
end

function love.focus(f)
    gameIsPaused = not f
    if gameIsPaused then
        for i, sound in ipairs(sounds) do
            print('sound')
        end
    end
end

function love.update(dt)
    if gameIsPaused then
        return
    end
    --
    if x_offset < wanted_x_offset then
        x_offset = x_offset + (wanted_x_offset - x_offset) / offset_frames
    end
    if x_offset > wanted_x_offset then
        x_offset = x_offset - (x_offset - wanted_x_offset) / offset_frames
    end
    --
    if y_offset < wanted_y_offset then
        y_offset = y_offset + (wanted_y_offset - y_offset) / offset_frames
    end
    if y_offset > wanted_y_offset then
        y_offset = y_offset - (y_offset - wanted_y_offset) / offset_frames
    end
end

function love.mousepressed(x, y, button, istouch)
   if button == 1 then
      click_x = x
      click_y = y
   end
end

function love.mousereleased(x, y, button, istouch)
   if button == 1 then
      wanted_x_offset = x_offset + x - click_x
      wanted_y_offset = y_offset + y - click_y
   end
end

function love.keypressed(key)
    if key == 'escape' then
        love.event.push('quit')
    end
end

function love.keyreleased(key)
   if key == 'b' then
      text = "The B key was released."
   elseif key == 'a' then
      a_down = false
   end
end

function love.draw()
    love.graphics.setColor(255, 255, 255)
    for y,line in ipairs(cube) do
        for x,visible in ipairs(line) do
            if visible > 0 then
                local x_pos = x * tile_size + (y % 2 + 1) * tile_size / 2 + x_offset
                local y_pos = y * tile_size / 4 - 0 * tile_size / 2 + y_offset
                love.graphics.draw(image, x_pos, y_pos)
            end
        end
    end
    love.graphics.setColor(0,0,0)
    love.graphics.print(text, 400, 300)
    love.graphics.print("FPS: "..love.timer.getFPS(), 0, 0)
end

function love.quit()
  print("Thanks for playing! Come back soon!")
end
