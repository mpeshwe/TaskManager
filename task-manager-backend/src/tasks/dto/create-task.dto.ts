/**
 * DTO for creating a new task
 * This defines the "contract" for what data is needed to create a task
 */
export class CreateTaskDto {
  /**
   * The title of the task (required)
   * @example "Complete NestJS tutorial"
   */
  title: string;

  /**
   * Optional description providing more details about the task
   * @example "Learn about modules, controllers, and services"
   */
  description?: string;
}
