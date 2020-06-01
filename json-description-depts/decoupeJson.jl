import JSON

cantons = Dict()
open("cantons_2015_simpl.json", "r") do f
    global cantons
    cantons=JSON.parse(f)
end

dep= filter(x -> x["properties"]["dep"] == "61", cantons["features"])
print(dep)
write("61.json", JSON.json(dep))

#=dep= filter(x -> x["properties"]["dep"] == "2A", cantons["features"])
write("2A.json", JSON.json(dep))

dep= filter(x -> x["properties"]["dep"] == "2B", cantons["features"])
write("2B.json", JSON.json(dep))

for idDep in 1:9
    dep = filter(x -> x["properties"]["dep"] == "0"*string(idDep), cantons["features"])
    write("0"*string(idDep)*".json", JSON.json(dep))
end


for idDep in 10:95
    dep = filter(x -> x["properties"]["dep"] == string(idDep), cantons["features"])
    write(string(idDep)*".json", JSON.json(dep))
end
=#
