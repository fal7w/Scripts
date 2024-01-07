const { WebhookClient, MessageEmbed } = require('discord.js');

const webhook = new WebhookClient(process.env.DISCORD_WEBHOOK);

const issueTitle = process.env.GITHUB_EVENT_ISSUE_TITLE;
const issueUrl = process.env.GITHUB_EVENT_ISSUE_HTML_URL;

const embed = new MessageEmbed()
  .setColor('#0099ff')
  .setTitle('New Issue Opened')
  .setDescription('A new issue has been opened in the repository.')
  .addFields(
    { name: 'Issue Title', value: issueTitle },
    { name: 'Issue URL', value: issueUrl }
  );

webhook.send('', {
  embeds: [embed],
});
