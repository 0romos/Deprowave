-- Import necessary modules
local rpc = import("discordrpc")
local shell = import("micro/shell")
local buffer = import("micro/buffer")
local config = import("micro/config")

-- Initialize the Discord RPC client
local discordRPC = nil
local presenceDetails = {}

local function initializeRPC()
    local clientID = config.GetGlobalOption("discordrpc_client_id")
    if clientID == nil or clientID == "" then
        micro.InfoBar():Error("Discord RPC client ID not set. Please configure 'discordrpc_client_id' in settings.json.")
        return
    end

    discordRPC = rpc.new(clientID)
    discordRPC:initialize()

    presenceDetails.largeImageKey = "micro_logo"
    presenceDetails.largeImageText = "Micro Editor"
    presenceDetails.smallImageKey = "editing_icon"
    presenceDetails.smallImageText = "Editing"
end

local function updatePresence()
    if discordRPC == nil then
        return
    end

    local currentBuffer = buffer.Buffer{}
    local currentPath = shell.getwd()

    presenceDetails.state = "Editing " .. currentPath
    presenceDetails.details = "Line " .. currentBuffer.Cursor.Loc.Y + 1

    discordRPC:updatePresence(presenceDetails)
end

-- Event handlers
local function onBufferOpen()
    updatePresence()
end

local function onBufferClose()
    updatePresence()
end

local function onBufferUpdate()
    updatePresence()
end

-- Enable or disable the Discord RPC integration
local function toggleIntegration(val)
    if val == "true" then
        initializeRPC()
        updatePresence()
        buffer.AddEventHandler(buffer.Open, onBufferOpen)
        buffer.AddEventHandler(buffer.Close, onBufferClose)
        buffer.AddEventHandler(buffer.Update, onBufferUpdate)
    else
        if discordRPC ~= nil then
            discordRPC:stop()
        end
        buffer.RemoveEventHandler(buffer.Open, onBufferOpen)
        buffer.RemoveEventHandler(buffer.Close, onBufferClose)
        buffer.RemoveEventHandler(buffer.Update, onBufferUpdate)
    end
end

-- Register the event handlers
config.AddRuntimeOptionChangeListener("discordrpc", toggleIntegration)
