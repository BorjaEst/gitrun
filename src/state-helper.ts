import * as core from '@actions/core'
import { UUID } from 'crypto'

/**
 * Indicates whether the action is running in the post phase
 */
export const IsPost = !!core.getState('isPost')

/**
 * The runnerId of the runner that is running the action
 */
export const RunnerId = core.getState('runnerId')


/**
 * Save the runnerId so the action can operate on the correct runner. 
 */
export function setRunnerId(runnerId: UUID) {
    core.saveState('runnerId', runnerId)
}


// Set default state1 to true
if (!IsPost) {
    core.saveState('isPost', 'true')
}