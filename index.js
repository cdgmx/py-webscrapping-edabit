const Discord = require ('discord.js');
const bot  = new Discord.Client();

const token = 'NzQwMTA1OTQxMzkwOTgzMjIx.XykLXg.AxGUQLOnPSDEnMCJv1f-Ivsotow';

const PREFIX = '!';






bot.on('ready', ()=>{
console.log('this bot is online!');
})



bot.on('message', msg=>{

if(msg.content === "Hello"){
    msg.reply('hello man');
    }
})

bot.login(token);

