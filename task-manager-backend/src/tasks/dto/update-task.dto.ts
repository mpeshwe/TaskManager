/**
 * DTO for updating an existing task
 * All fields are optional because we might only want to update one field
 */
export class UpdateTaskDto {
  /**
   * Optional new title for the task
   */
  title?: string;

  /**
   * Optional new description for the task
   */
  description?: string;

  /**
   * Optional completion status
   */
  completed?: boolean;
}
