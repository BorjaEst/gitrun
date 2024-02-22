import * as core from '@actions/core'
import * as coreCommand from '@actions/core/lib/command'
import * as gitRunProvider from './git-runner-provider'
import * as inputHelper from './input-helper'
import * as path from 'path'
import * as stateHelper from './state-helper'

async function run(): Promise<void> {
    try {
        const sourceSettings = await inputHelper.getInputs()

        try {
            // Register problem matcher
            coreCommand.issueCommand(
                'add-matcher',
                {},
                path.join(__dirname, 'problem-matcher.json')
            )

            // TODO: Run the action
            console.log('Run github runner in ai4eosc')

        } finally {
            // Unregister problem matcher
            coreCommand.issueCommand('remove-matcher', { owner: 'checkout-git' }, '')
        }
    } catch (error) {
        core.setFailed(`${(error as any)?.message ?? error}`)
    }
}

async function cleanup(): Promise<void> {
    try {
        await gitRunProvider.cleanup(stateHelper.RunnerId)
    } catch (error) {
        core.warning(`${(error as any)?.message ?? error}`)
    }
}

// Main
if (!stateHelper.IsPost) {
    run()
}
// Post
else {
    cleanup()
}