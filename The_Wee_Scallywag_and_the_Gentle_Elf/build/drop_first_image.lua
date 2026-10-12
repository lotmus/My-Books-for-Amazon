local dropped = false
function Para(el)
  if not dropped and #el.content == 1 and el.content[1].t == "Image" then
    dropped = true
    return {}
  end
end
