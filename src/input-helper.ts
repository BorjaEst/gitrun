import * as core from '@actions/core'
import { IGitSourceSettings } from './git-runner-settings'

export async function getInputs(): Promise<IGitSourceSettings> {
    const result = ({} as unknown) as IGitSourceSettings

    // Access token to authenticate with the platform
    result.authToken = core.getInput('at', { required: true })

    // Virtual organization to use
    result.virtualOrganization = core.getInput('vo', { required: true })

    // The jit configuration string to use
    result.jitConfig = core.getInput('jit-config', { required: true })

    return result
}